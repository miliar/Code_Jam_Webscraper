#!/usr/bin/python

import sys

def solveCase(values):
  n=1
  hits=0
  for i in values:
    if i!=n:
      hits+=1
    n+=1
  return hits

n=0
for row in sys.stdin:
  if n and (n%2==0): # Skip first row that is just a count
    rowArray = row.split(' ')
    print "Case #%s: %s.000000" % (n/2,solveCase(map(int,rowArray)))
  n=n+1

