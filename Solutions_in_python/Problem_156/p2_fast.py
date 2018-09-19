#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import heapq

count = None
num_diners = None
tests = []
for line in sys.stdin:
  if not count:
    count = int(line.strip())
    continue
  elif not num_diners:
    num_diners = int(line.strip())
  else:
    s = line.strip().split()
    if len(s) != num_diners:
      print "Wrong string length on line (%d):" % num_diners, line
      sys.exit(0)
    tests.append([int(x) for x in s])
    num_diners = None

if count != len(tests):
  print "Wrong number of test cases"
  sys.exit(0)
    

max_stack = 1000
times = []
for i in xrange(0, max_stack + 1):
  time = [i,]
  #num_special_minutes
  #print i
  for j in xrange(1, i):
    #print i, j, (i+j)/(j+1) + j
    t = (i+j)/(j+1) + j
    if t >= time[j-1]:
      break
    time.append(t)
  #print i, times
  for j in xrange(len(time)):
    time[j] -= j
  #print i, times
  times.append(time)

#print times

def solve(test):
  hist = {}
  for i in test:
    hist[i] = hist.get(i, 0) + 1

  heights = sorted(hist.items(), key = lambda x: x[0], reverse = True)
  heap = []
  for h in heights:
    heap.append((-h[0], [h[0], h[1], 0]))

  best = heights[0][0]
  #print heap
  heapq.heapify(heap)
  #print heap

  special = 0
  h = best
  while 1:
    top = heapq.heappop(heap)
    #print top
    d = top[1][0]
    i = top[1][2]
    if i +1 >= len(times[d]):
      break
    #print times[d], len(times[d]), i
    next = times[d][i+1]
    special += top[1][1]
    top[1][2] += 1
    heapq.heappush(heap, (-times[d][i+1], top[1]))
    h = max(next, -heap[0][0])
    if h + special < best:
      best = h + special

  return best


counter = 0
for t in tests:
  counter += 1
  print "Case #%d: %d" % (counter, solve(t))





