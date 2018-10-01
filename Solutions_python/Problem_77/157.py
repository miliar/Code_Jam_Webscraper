#!/usr/bin/env python

T = int(raw_input())
for case in range(T):
  N = int(raw_input())
  vals = [int(c) for c in raw_input().split(' ')]
  unsorted = len(vals)
  for idx, val in enumerate(vals):
    if idx+1 == val:
      unsorted = unsorted - 1
  print 'Case #%i: %i.000000' % (case+1, unsorted)
