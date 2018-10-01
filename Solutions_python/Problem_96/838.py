#!/usr/bin/python
import sys
data=["3 1 5 15 13 11","3 0 8 23 22 21","2 1 1 8 0","6 2 8 29 20 8 18 18 21"]
if len(sys.argv)>2:
  inf = sys.argv[1]
  outf = sys.argv[2]
if len(sys.argv)>1:
  infi = sys.argv[1]
  data = []
  fi = open(infi)
  lines = fi.readlines()
  d = 0
  for line in lines:
    if d!=0:
      line = line.replace("\n","")
      data.append(line)
    d+=1
d = 1
for dat in data:
  datsplit = dat.split(" ");
  n = int(datsplit[0])
  s = int(datsplit[1])
  p = int(datsplit[2])
  c = []
  for i in range(3,len(datsplit)):
    c.append(int(datsplit[i]))
  minnormal = p*3-2
  minser    = p*3-4
  if minnormal<0:
    minnormal =0
  if minser<0:
    minser=1
  numnormal = 0
  numser    = 0
  for i in c:
    if i>=minnormal:
      numnormal +=1
    elif i>=minser:
      numser +=1
  if numser>s:
    numser=s
  print "Case #"+str(d)+": "+str(numnormal+numser)
  d+=1
