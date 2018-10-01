#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os, shutil, subprocess
import signal
import re
import math, random
import numpy as np

sys.setrecursionlimit(2000000000)
signal.signal(signal.SIGINT, signal.SIG_DFL)



def test(verbose):
  ac, aj = map(int, input().split())
  
  C, J = [], []
  
  for _ in range(ac):
    b, e = map(int, input().split())
    C.append([b, e])
  
  for _ in range(aj):
    b, e = map(int, input().split())
    J.append([b, e])
  
  if not verbose:
    return
  
  if len(C) == len(J) == 0:
    print(1)
    return
  
  N = 1440
  M = np.zeros(N, dtype=np.int)
  
  for b, e in C: M[b:e] = 1
  for b, e in J: M[b:e] = 2
  
  cl = 720 - np.sum(M == 1)
  jl = 720 - np.sum(M == 2)
  
  U = []
  i0 = None
  for i in range(N):
    if M[i] == 0:
      if i0 is None:
        i0 = i
    else:
      if i0 is not None:
        U.append([i0, i])
      i0 = None
  if i0 is not None:
    if U[0][0] == 0:
      U[0][0] = i0
    else:
      U.append([i0, N])
  
  U.sort(key = lambda t: (t[1] - t[0]) % N)
  
  for b, e in U:
    bb = (b - 1) % N
    ae = (e + 1) % N
    ul = (e - b) % N
    if M[bb] == M[ae] == 1 and ul <= cl:
      if b < e:
        M[b:e] = 1
      else:
        M[e:] = 1
        M[:b] = 1
      cl -= ul
    if M[bb] == M[ae] == 2 and ul <= jl:
      if b < e:
        M[b:e] = 2
      else:
        M[e:] = 2
        M[:b] = 2
      jl -= ul
  
  i = N - 1
  prev = M[i]
  pnoz = prev
  while pnoz == 0:
    i -= 1
    pnoz = M[i]
  
  ans = 0
  for i in range(N):
    if M[i] != prev:
      if prev != 0:
        ans += 1
      if prev == 0 and pnoz == M[i]:
        ans += 1
      prev = M[i]
    if M[i] != 0 and M[i] != pnoz:
      pnoz = M[i]
  
  print(max(2, ans))


if __name__ == '__main__':
  z = int(sys.argv[1]) if len(sys.argv) > 1 else -1

  t = int(input())
  for i in range(1, t+1):
    verbose = z in (-1, i)
    if verbose:
      print('Case #%d: ' % i, end='')
    test(verbose)

