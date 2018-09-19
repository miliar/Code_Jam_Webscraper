#!/usr/bin/python

import sys

def calculate_removed(a, motes, i, j):
  ops = 0
  for k in xrange(i, j+1):
    if motes[k] > 2 * a - 1:
      ops += 1
  return ops

def calculate_deep(a, motes, i):
  n = motes[i]
  ops = 0
  while motes[i] >= a:
    a += a - 1
    ops += 1
  a += motes[i]
  na = a
  j = i - 1
  for m in motes[i:]:
    if m < a:
      a += m
      j += 1
    else:
      break
  return ops, j, na

def Solve():
  a, n =  map(int,sys.stdin.readline().split())
  motes = map(int,sys.stdin.readline().split())
  motes.sort()
  ops = 0
  if a == 1:
    return len(motes)
  for i in xrange(0, len(motes)):
    if motes[i] < a:
      a += motes[i]
      continue
    if motes[i] < (a + a - 1):
      a += a - 1
      a += motes[i]
      ops += 1
    else:
      add_ops, j, na = calculate_deep(a, motes, i)
      if calculate_removed(a, motes, i, j) >= add_ops:
        ops += add_ops
        a = na
      else:
        ops += 1
  return ops

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %d" % (case, Solve())
