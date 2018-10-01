#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

if len(sys.argv)<2:
  print "gimme data..."
  sys.exit(1)

inf_name=sys.argv[1]
outf_name=inf_name[:-2]+'out'
inf=open(inf_name,'r')
outf=open(outf_name,'w')
N=line=inf.next().split()[0]
C=1
for line in inf:
  ff=line.split()[0]
  print ff
  number=[int(i) for i in list(ff)]
  nums=sorted(number)
  i=len(number)-1
  while i>0 and int(number[i])<=int(number[i-1]):
    i-=1
  if i==0:
    nums.append(0)
    nums=sorted(nums)
    for j in xrange(len(nums)):
      if nums[j]<>0:
	break
    newnum=[nums.pop(j)]
    newnum.extend(nums)
  else:
    end=number[i-1:]
    #print end
    end=sorted(end)
    for j in xrange(len(end)):
      if number[i-1]<end[j]:
	break
    newnum=number[:(i-1)]
    newnum.append(end[j])
    end.remove(end[j])
    newnum.extend(end)
  newnum=map(str,newnum)  
  print "Case #"+str(C)+": "+"".join(newnum)
  outf.write("Case #"+str(C)+": "+"".join(newnum)+"\n")
  C+=1

outf.close()
inf.close()

