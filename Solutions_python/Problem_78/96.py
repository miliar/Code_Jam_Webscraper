#!/usr/bin/python

import sys,re

if len(sys.argv) != 2:
  print "usage: " + sys.argv[0] + " infile"
  sys.exit()
infile = open(sys.argv[1], 'r')

def handleonecase(line1):
  #TODO
  N = int(line1[0])
  PD = int(line1[1])
  PG = int(line1[2])
  #print N, PD, PG
  if PD == 0:
    if PG == 100: return "1Broken"
  elif PD == 100:
    if PG == 0: return "2Broken"
  elif PG == 100 or PG == 0: return "3Broken"

  if N >= 100: return "4Possible"

  for i in range(1, N+1):
    #print i
    if i*PD*.01 == int(i*PD*.01): 
      return "5Possible"

  return "6Broken"


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
  print "Case #" + str(casenum) + ": " + str(result)[1:]




