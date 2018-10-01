#!/usr/bin/python

import sys,re

if len(sys.argv) != 2:
  print "usage: " + sys.argv[0] + " infile"
  sys.exit()
infile = sys.argv[1]


def compute(candyvals):
  if len(candyvals) < 1: return "NO"
  xor = 0
  sum = 0
  smallest = int(candyvals[0])
  for candyval in candyvals:
    xor = xor ^ int(candyval)
    sum = sum + int(candyval)
    smallest = min(smallest, int(candyval))
  if xor: return "NO"
  return str(sum-smallest)




maxcases = 0
linenum = 0
casenum = 0
indata = open(infile, 'r').read().split('\n')

for line in indata:
  linenum = linenum + 1
  if linenum == 1:
    maxcases = int(line)
    continue

  if casenum >= maxcases:
    break

  if linenum %2 == 0:
    numcandies = int(line)
    continue

  casenum = casenum + 1
  candyvals = line.split()

  result = compute(candyvals)
  print "Case #" + str(casenum) + ": " + result






