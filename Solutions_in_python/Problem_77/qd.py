#!/usr/bin/python

import os
import sys

fn = sys.argv[1]

fh = open(fn, "r")
T = int(fh.readline().strip())
cases = []
for i in range(T):
  fields = fh.readline().strip().split()
  N = int(fields[0])
  fields = fh.readline().strip().split()
  n_s = map(lambda x: int(x), fields)
  if len(n_s)!=N:
    print "read error"
  cases += [n_s]

#print cases

try:
  line = fh.readline().strip()
  if line == "":
    print "good read"
except:
  print "good read"

fh.close()



fh = open("out.txt","w")
for (i,case) in enumerate(cases):
  n_s = case
  i_s = map(lambda x: x+1, range(len(n_s)))
  cycles = map(lambda x: 0, range(len(n_s)))
  ordered = map(lambda x: 0, range(len(n_s)))
  for j in range(len(n_s)):
    if n_s[j]==i_s[j]:
      ordered[j]=1
  cyc = 0
  while sum(ordered)!=len(ordered):
    cyc+=1
    for j in range(len(ordered)):
      if ordered[j]==0:
        break
    cycles[j]=cyc
    next_l = n_s[j]-1
    ordered[j] = 1
    while next_l != j:
      cycles[next_l] = cyc
      ordered[next_l]=1
      next_l = n_s[next_l]-1
  counts = map(lambda x: 0, range(cyc+1))
  for j in range(len(cycles)):
    counts[cycles[j]]+=1
  #print cycles, counts, sum(counts[1:])
  print >> fh, "Case #"+str(i+1)+": " + str(sum(counts[1:]))

fh.close()

