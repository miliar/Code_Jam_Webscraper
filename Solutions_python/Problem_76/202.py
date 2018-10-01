#!/usr/bin/python

import sys

def solveCase(values):
  if reduce(lambda x,y:x^y,values):
    return "NO"
  return sum(values)-min(values)

n=0
for row in sys.stdin:
  if n and (n%2==0): # Skip first row that is just a count
    rowArray = row.split(' ')
    print "Case #%s: %s" % (n/2,solveCase(map(int,rowArray)))
  n=n+1

