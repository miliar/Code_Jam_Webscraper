#!/usr/bin/python

import os
import sys

fn = sys.argv[1]

fh = open(fn, "r")
T = int(fh.readline().strip())
cases = []
for i in range(T):
  fields = fh.readline().strip().split()
  C = int(fields[0])
  fields = fields[1:]
  c_s = fields[:C]
  fields = fields[C:]
  D = int(fields[0])
  fields = fields[1:]
  d_s = fields[:D]
  fields = fields[D:]
  N = int(fields[0])
  n_s = fields[1:]
  if len(n_s)>1:
    print "read error"
  if len(n_s[0])!=N:
    print "read error"
  cases += [[c_s, d_s, n_s[0]]]

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
  [c_s, d_s, str1] = case
  d_c = {}
  for c in c_s:
    d_c[c[0]+c[1]]=c[2]
    d_c[c[1]+c[0]]=c[2]
  result = ""
  for j in str1:
    result += j
    if len(result)>1:
      if result[-2:] in d_c:
        result = result[:-2]+d_c[result[-2:]]
    if len(result) > 1:
      bads = filter(lambda x: result[-1] in x, d_s)
      for bad1 in bads:
        if bad1[0] in result and bad1[1] in result:
          result = ""
  print >> fh, "Case #"+str(i+1)+": ["+", ".join(result)+"]"

fh.close()

