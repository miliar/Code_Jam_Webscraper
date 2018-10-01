#!/usr/bin/python

import sys,re

if len(sys.argv) != 2:
  print "usage: " + sys.argv[0] + " infile"
  sys.exit()
infile = sys.argv[1]


def E(n):
  if n < 2: return 0
  return n

def countNumInWrongPlace(l):
  c = 0
  for i in range(0, len(l)):
    if i+1 != int(l[i]): c = c +1
  return c

def f(l):
  return E(countNumInWrongPlace(l))

maxcases = 0
linenum = 0
casenum = 0

indata = open(infile, 'r').read().split('\n')
for line in indata:
  linenum = linenum + 1
  if linenum == 1:
    maxcases = int(line)
    continue

  if linenum %2 == 0:
    continue

  casenum = casenum + 1
  if casenum > maxcases:
    break

  l = line.split()
  result = f(l)
  print "Case #" + str(casenum) + ": " + str(result)





