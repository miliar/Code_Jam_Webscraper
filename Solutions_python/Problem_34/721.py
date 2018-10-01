#!/usr/bin/python

import os,sys,re

curpath=os.path.dirname(__file__)

infile = open(curpath+"/A-large.in","r")
outfile = open(curpath+"/out.txt","w")
temp = infile.readline().split(" ")
l = int(temp[0])
d = int(temp[1])
n = int(temp[2])
words = []

def repx(str) :
  return str.replace("(","[").replace(")","]")

for i in range (0,d) :
  words.append(infile.readline())
for i in range (0,n) :
  temp = infile.readline()
  c = 0
  for j in words :
    p = re.compile(repx(temp))
    if p.match(j) is not None:
      c = c + 1
  
  print "Case #"+str(i+1)+": "+str(c)
  outfile.write("Case #"+str(i+1)+": "+str(c)+"\n")