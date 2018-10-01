#!/usr/bin/env python

"""
Contest: Google Code Jam Round 1C
Problem: 
"""

from decimal import *
getcontext().rounding = ROUND_HALF_UP
import math
import sys


input_file = open(sys.argv[1])

numcases = int(input_file.readline().strip())
for i in xrange(1, numcases+1):
  fields = input_file.readline().split()
  L, t2, N, C = int(fields[0]), int(fields[1]), int(fields[2]), int(fields[3])
  ai = map(int, fields[4:])
  dists = []
  can_build = False
  t_star = 0
  t_star_dist = 2*ai[0]
  t = t2
  for n in xrange(0, N):
    cur_dist = 2*ai[n % C]
    t -= cur_dist
    if t <= 0:
      t_star = n
      t_star_dist = -t
      can_build = True
      break
  time = 0
  if can_build:
    time += t2
    dists.append(t_star_dist)
    for n in xrange(t_star+1, N):
      cur_dist = 2*ai[n % C]
      dists.append(cur_dist)
    dists.sort()
    dists.reverse()
    for l in xrange(0, L):
      time += (dists[l] / 2)
    for x in xrange(L, len(dists)):
      time += dists[x]
  else:
    for x in xrange(0, N):
      time += 2*ai[x % C]
  print("Case #%d: %d" % (i, time))