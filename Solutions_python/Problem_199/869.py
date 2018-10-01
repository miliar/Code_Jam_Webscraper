#!/usr/bin/env python3

from sys import stdin as I
from queue import Queue

def solve(T):
  S, K = tuple(I.readline().split(' '))
  K = int(K)

  q = Queue()
  flips = 0
  expected = '+'

  for i in range(len(S)):
    s = S[i]
    _expected = expected
    if s != expected:
      q.put(i + K -1)
      flips += 1
      expected = '-' if expected == '+' else '+'

    if not q.empty() and q.queue[0] == i:
      q.get()
      expected = '-' if expected == '+' else '+'

  if q.empty():
    print("Case #%i: %i" % (T, flips))
  else:
    print("Case #%i: IMPOSSIBLE" % T)

T = int(I.readline())
for i in range(T):
  solve(i + 1)
