#!/usr/bin/env python
import os
import sys
import time

tStart = time.time()

#---------------------------------------------------------------------

ifilename = 'input.in'
ofilename = 'results.out'

args = sys.argv
if len(args) > 1:
  ifilename = args[1]
if len(args) > 2:
  ofilename = args[2]

#---------------------------------------------------------------------
 
ifile = open(ifilename,'r')
data  = ifile.read()
ifile.close()
lines = data.splitlines()
ofile = open(ofilename, 'w')

#---------------------------------------------------------------------
# Functions
def process(D,cases):

  max_time = (D-cases[0][0])/cases[0][1]
  for case in cases[1:]:
    time = (D-case[0])/case[1]
    max_time = max([max_time, time])

  vel = D/max_time

  return '%.9f'%(vel)

#---------------------------------------------------------------------
# Main
ncases = int(lines[0])
lines  = lines[1:]
for ncase in xrange(ncases):
  data  = lines[0].split()
  lines = lines[1:]
  D     = int(data[0])
  N     = int(data[1])
  cases = []
  for k in xrange(N):
    cases.append([float(x) for x in lines[0].split()])
    lines = lines[1:]

  solution = process(D,cases)

  # -------------------------------------------------
  res = 'Case #%d: %s'%(ncase+1, solution)
  ofile.write('%s\n'%(res))
  print res

#---------------------------------------------------------------------

ofile.close()

print '\n Run time = ' + str((time.time() - tStart))     
