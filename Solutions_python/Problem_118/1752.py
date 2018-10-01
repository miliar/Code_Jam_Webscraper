#!/usr/bin/python

import sys
import math

def isfair(x):
  s = str(x)
  for i in range(len(s)/2):
    if s[i] != s[len(s)-1-i]:
      return False
  return True

def isfairsquare(x):
  if not isfair(x):
    return False
  r = int(math.sqrt(x))
  if r*r != x:
    return False
  return isfair(r)

T = int(sys.stdin.readline())
for t in range(T):
  toks = sys.stdin.readline().strip().split()
  A = int(toks[0])
  B = int(toks[1])
  # print A,B

  s = 0
  for x in xrange(A,B+1):
    if isfairsquare(x):
      s += 1
      # print x,"!"

  print "Case #%d: %d" % (t+1, s)

