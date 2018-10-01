#!/usr/bin/python -u

import sys,re

if len(sys.argv) != 2:
  print "usage: " + sys.argv[0] + " infile"
  sys.exit()
infile = open(sys.argv[1], 'r')

debugprint = 10

def debug(str, lvl=5):
  if debugprint > lvl: print "[DEBUG]", str

def guaranteed(N,P):
  if(pow(2,N)==P): return pow(2,N)-1
  b = 1
  while(P>pow(2,N-1)):
    P = P - pow(2,N-1)
    N = N - 1
    b = b + 1
  return pow(2,b)-2

def possible(N,P):
  NN = N
  if(pow(2,N)==P): return pow(2,N)-1
  if(P==1): return 0
  b = 1
  while(P<pow(2,N-1)):
    N = N - 1
    b = b + 1
  return pow(2,NN)-pow(2,b)

def handleonecase(line1):
  #TODO
  N = long(line1[0])
  P = long(line1[1])
  part1 = guaranteed(N,P)
  part2 = possible  (N,P)
  return str(part1) + ' ' + str(part2)

maxcases = 0
casenum = 0

line = infile.readline().strip()
maxcases = int(line)
while line:
  casenum = casenum + 1
  if casenum > maxcases: break
  line1 = infile.readline().strip().split()
#  line2 = infile.readline().strip().split()
  result = handleonecase(line1)
  print "Case #" + str(casenum) + ": " + str(result)




