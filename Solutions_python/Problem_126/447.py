#!/usr/bin/python

import os,sys,string

def is_consonant(char):
  if char=="a":
    return 0
  elif char=="e":
    return 0
  elif char=="i":
    return 0
  elif char=="o":
    return 0
  elif char=="u":
    return 0
  else:
    return 1

def n_combinations(i,n,l_r,l_l):
  forwards=l_r-(i+n-1)
  backwards=(i+1)-l_l
  return forwards*backwards

fname=sys.argv[1]
fhandle=open(fname,"r")

ncases=int(fhandle.readline())

for case in range(ncases):
  prefix="Case #"+str(case+1)+": "

  [name,n]=fhandle.readline().rstrip().split(" ")
  n=int(n)
  l=len(name)

  count=[0]*l
  for i in range(l):
    increment=is_consonant(name[i])
    if increment>0:
      min_i=max(i-(n-1),0)
      for j in range(min_i,i+1):
        count[j]+=increment
  n_count=0
  l_l=0
  for i in range(l-(n-1)):
    if count[i]>=n:
      n_count+=n_combinations(i,n,l,l_l)
      l_l=i+1

  print prefix+str(n_count)
