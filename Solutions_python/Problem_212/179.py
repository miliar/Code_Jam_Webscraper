#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import random


def solve(p, g):
  #print p, g
  h = {0:0, 1:0, 2:0, 3:0}
  for x in g:
    h[x] += 1

  #p = 4
  #if p == 4:
  #  print "quack"
  #  h = {0:7, 1:11, 2:9, 3:18}

  #print p,h
  fresh = h[0]
  h[0] = 0
  #print "zeros: ", fresh, h


  if p == 2:
    if h[1] > 0:
      fresh += (h[1]-1)/2 + 1

  elif p == 3:
    y = min(h[1], h[2])
    fresh += y
    #print "pairs: ", fresh

    if h[1] > y:
      y = h[1] - y
      fresh += (y-1)/3 + 1
    elif h[2] > y:
      y = h[2] - y
      fresh += (y-1)/3 + 1

    #print "alts: ", fresh


  elif p == 4:
    y = h[2] - (h[2] % 2)
    fresh += y/2
    h[2] -= y
    #print "2 pairs:", fresh, h

    y = min(h[1], h[3])
    fresh += y
    h[1] -= y
    h[3] -= y
    #print "1/3 pairs:", fresh, h

    if h[2] and h[1] >=2:
      fresh += 1
      h[2] -= 1
      h[1] -= 2
    elif h[2] and h[3] >=2:
      fresh += 1
      h[2] -= 1
      h[3] -= 2

    #print "leftover 2:", fresh, h

    
    y = h[1] / 4
    fresh += y
    h[1] -= y*4

    #print "1 groups:", fresh, h

    y = h[3] / 4
    fresh += y
    h[3] -= y*4

    #print "3 groups:", fresh, h

    if h[1] > 0 or h[2] > 0 or h[3] > 0:
      fresh += 1
      #print "leftovers", fresh, h


  return fresh
 

total = None
count = 0
f = sys.stdin

count = None
tests = []
n, p = None, None
for line in sys.stdin:
  if not count:
    count = int(line.strip())
    continue
  elif not n:
    n, p = [int(x) for x in line.strip().split()]
  else:
    tests.append((p, sorted([int(x) % p for x in line.strip().split()])))
    n, p = None, None 

if count != len(tests):
  print "Wrong number of test cases"
  sys.exit(0)

counter = 0
for s in tests:
  counter += 1
  #print t
  print "Case #%d: %d" % (counter, solve(*s))
  #sys.exit()



