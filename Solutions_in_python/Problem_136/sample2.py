#!/usr/bin/env python
import sys, math

def cal(C, F, X, s):
  return sum(map(lambda x: C/(2.0 + x*F), range(0, s))) + X / (2.0 + s*F)

def dcal(C, F, X, s, t):
  return (2.0 + s * F) * t

fp = open("sample5.txt", "rt")
nTestCase = int(fp.readline())
for i in range(0, nTestCase):
  data = map(lambda x: float(x), fp.readline().strip().split())
  C, F, X = data[0], data[1], data[2]
  print "Case #%d: %3.7f" % (i+1, min([cal(C, F, X, s) for s in range(0, int(math.ceil(X)))]))
