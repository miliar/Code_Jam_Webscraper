#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import random
import copy


def solve(d, h):
  #print d, h

  slowest = None
  for s, v in h:
    finish = float((d-s)) / v
    #print s, v, finish
    if not slowest or finish > slowest:
      slowest = finish

  return d / slowest

total = None
count = 0
f = sys.stdin

count = None
d, n = None, None
next = None
tests = []
for line in sys.stdin:
  if not count:
    count = int(line.strip())
    continue
  elif d == None:
    d, n = [int(x) for x in line.strip().split()]
    next = []
  else:
    next.append([int(x) for x in line.strip().split()])
    if len(next) == n:
      tests.append((d, next))
      d, n = None, None
      next = []

if count != len(tests):
  print "Wrong number of test cases"
  sys.exit(0)

counter = 0
for s in tests:
  counter += 1
  #print t
  print "Case #%d: %.6f" % (counter, solve(*s))
  #sys.exit()



