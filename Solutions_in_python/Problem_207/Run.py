#!/usr/bin/python
# -*- coding: latin-1 -*-
import os
import sys
import numpy as np
import operator
from operator import itemgetter
import math

def sortRYB(R,Y,B):

  V = []
  I = []
  if R >= Y and R >= B:
    V = [R,Y,B] if Y >= B else [R,B,Y]
    I = ['R','Y','B'] if Y >= B else ['R','B','Y']
  elif Y >= R and Y >= B:
    V = [Y,R,B] if R >= B else [Y,B,R]
    I = ['Y','R','B'] if R>=B else ['Y','B','R']
  else:
    V = [B,Y,R] if Y >= R else [B,R,Y]
    I = ['B','Y','R'] if Y >= R else ['B','R','Y']
  
  return V,I

def allEquals(S):
  val = S[0]
  for s in S:
    if s > 0:
      val = s
      break
  
  for s in S:
    if s > 0 and s != val:
      return False
  
  return True

def solve(N, R, O, Y, G, B, V):
  S = [R, O, Y, G, B, V]
  T = ['R', 'O', 'Y', 'G', 'B', 'V']
  n = 0
  res = ""
  
  mVal = max(T)
  for s in S:
    mVal = min(mVal, s) if s > 0 else mVal
  #print "mVal = ", mVal
  
  pInd = -1
  while n < N:
    if allEquals(S):
      break
    #print S
    val, ind = 0, 0
    for k in xrange(len(S)):    
      val, ind = (S[k], k) if S[k] >= val and k != pInd else (val, ind)
    res += T[ind]
    S[ind] -= 1
    n += 1
    pInd = ind
    
  print "res = ", res
  print "S = ", S, ", T = ", T
  I = []
  
  if n == 0:
    for k in xrange(len(T)):
      if S[k] > 0:
        I.append(k)
  else:
    for k in xrange(len(T)):
      if res[-1] != T[k] and S[k] > 0 and T[k] != res[0]:
        I.append(k)
        break
    for k in xrange(len(T)):
      if S[k] > 0 and T[k] == res[0]:
        I.append(k)
        break
    for k in xrange(len(T)):
      if S[k] > 0 and k not in I:
        I.append(k)
        break
  print "I = ", I
  
  while n < N:
    for i in I:
      if S[i] > 0:
        res += T[i]
        S[i] -= 1
        n += 1
    
  print res
  
  for k in xrange(len(res)):
    if res[k] == res[k-1]:
      return "IMPOSSIBLE"
  if len(res) != N:
    print "len(res) = ", len(res), ", N = ", N
    return "error"
  return res
  
def main():
  
  # Open the file to read
  file = open("Test.txt", "r")
  
  # Read the file
  T = int(file.readline())
  answer = []

  # Read the cases
  for i in xrange(T):
    
    N, R, O, Y, G, B, V = [int(k) for k in file.readline().split(' ')]
    print N, R, O, Y, G, B, V
    
    # Solve them
    answer.append("Case #" + str(i + 1) + ": " + solve(N, R, O, Y, G, B, V) + "\n")
    print answer[-1]
    
  # Close the file to read
  file.close()
  
  # Write the answer
  file = open("answer.txt", "w")
  for a in answer:
    file.write(a)
  file.close()

if __name__ == '__main__':
    main()