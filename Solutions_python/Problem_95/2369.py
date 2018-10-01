#!/usr/bin/env python

import os, numpy, math, sys, string


infile = open('key.in',"r")
key_in = infile.readlines()
infile.close()

T=int(key_in[0])
print T

infile = open('key.out',"r")
key_out = infile.readlines()
infile.close()

km_in=[]
km_out=[]
key_map={}

print "Creating a key"


for t in range(0,T):
  km_in += list(key_in[t+1].strip())
  km_out += list(key_out[t][9:].strip())

print len(km_in)
print len(km_out)

for i in list(string.lowercase):
  key_map[i] = ''

for i in range(0, len(km_in)):
  if (km_in[i] in key_map):
    key_map[km_in[i]] = km_out[i]


alphab = list(string.lowercase)
key_map['q'] = 'z'


#Find bsending letter
for k, v in key_map.iteritems():
  #print v
  if (v):
    alphab.remove(v)
    

key_map['z']=alphab[0]



infile = open(sys.argv[1],"r")
lines = infile.readlines()
infile.close()

T=int(lines[0])

output = ''

print T

for t in range(T):
  line=lines[1+t].strip()
  s=''
  for i in line:
    if not(i==' '):
      s+=key_map[i]
    else:
      s+=' '
    
  output += 'Case #%d: %s\n' % (t+1, s)

print output
file(sys.argv[1]+'.res','w').write(output)

