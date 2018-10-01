#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import random
import math

def solve(x):

  r,o,y,g,b,v = x
  if o > 0 or g > 0 or v > 0:
    return "IMPOSSIBLE"
  if r + o + y + g + b + v == 0:
    return "IMPOSSIBLE"
  #print x

  if r > y + b or y > r + b or b > y + r:
    return "IMPOSSIBLE"

  A, B, C = None, None, None
  p = None

  if r >= y and y >= b:
    A, B, C = r, y, b
    p = ["R", "Y", "B"]
  elif r >= b and b >= y:
    A, B, C = r, b, y
    p = ["R", "B", "Y"]
  elif b >= y and y >= r:
    A, B, C = b, y, r
    p = ["B", "Y", "R"]
  elif b >= r and r >= y:
    A, B, C = b, r, y
    p = ["B", "R", "Y"]
  elif y >= r and r >= b:
    A, B, C = y, r, b
    p = ["Y", "R", "B"]
  elif y >= b and b >= r:
    A, B, C = y, b, r
    p = ["Y", "B", "R"]
  else:
    assert False
  
  solution = ""
  doubles = B+C - A
  return (p[0] + p[1] + p[2]) * doubles + (p[0] + p[1]) * (B - doubles) + (p[0] + p[2]) * (C - doubles)

total = None
count = 0
f = sys.stdin

count = None
n, p = None, None
r = None
next = None
tests = []
for line in sys.stdin:
  if not count:
    count = int(line.strip())
    continue
  else:
    tests.append([int(x) for x in line.strip().split()][1:])

if count != len(tests):
  print "Wrong number of test cases"
  sys.exit(0)

'''
for i in range(10000):
  r = random.choice(range(10))
  o = random.choice(range(1))
  y = random.choice(range(10))
  g = random.choice(range(1))
  b = random.choice(range(10))
  v = random.choice(range(1))

  t = [r,o,y,g,b,v]
  s = solve(t)
  print s
  if s != "IMPOSSIBLE":
    assert r == len([x for x in s if x == "R"])
    assert y == len([x for x in s if x == "Y"])
    assert b == len([x for x in s if x == "B"])
    for i in xrange(len(s)-1):
      assert s[i] != s[i+1]
    assert s[0] != s[-1]
'''


counter = 0
for x in tests:
  counter += 1
  #print t
  print "Case #%d: %s" % (counter, solve(x))
  #sys.exit()

