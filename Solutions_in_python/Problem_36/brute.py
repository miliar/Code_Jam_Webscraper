#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

if len(sys.argv)<2:
  print "give me data..."
  sys.exit(1)

def printvalue():
  s=''
  for k,v in value.items():
    s+=text[k]+': '+str(v)+', '
  print s
def printcounter():
  s=''
  for k,v in counter.items():
    s+=text[k]+': '+str(v)+', '
  print s

inf_name=sys.argv[1]
outf_name=inf_name[:-2]+'out'
inf=open(inf_name,'r')
outf=open(outf_name,'w')
N=line=inf.next().split()[0]
C=1
w=''
invalid=False
text="welcome to code jam"
rtext="maj edoc ot emoclew"
#text="abc"
#rtext="cba"

firstc=text[0]

for line in inf:
  line=line[:-1]
  last_M=line.rfind(rtext[0])
  first_W=line.find(text[0])
  line=line[first_W:last_M+1]
  l=""
  for k in line:
    if k in text:
      l+=k
  line=l
  counter={}
  value={}
  for i in xrange(len(text)):
    counter[i]=0
    value[i]=0
  llen=len(line)
  tlen=len(text)
  for i in xrange(len(line)):
    for j in xrange(len(text)):
      
      if line[llen-1-i]==text[j]:
	#printcounter()
	#printvalue()
	if j==tlen-1:
	  counter[j]+=1
	  value[j]=counter[j]
	else:
	  if counter[j+1]>0:
	    counter[j]+=1
	    value[j]=(value[j]+value[j+1])%10000
	#printcounter()
	#printvalue()
	#print i,j,line[llen-1-i],text[j],counter[j],value[j]
	continue
  #print "Case #"+str(C)+": "+str(w)[0:4]
  #outf.write("Case #"+str(C)+": "+str(w)[0:4]+"\n")
  print "Case #"+str(C)+": "+str(value[0]).zfill(4)
  printvalue()
  print line+'\n'
  outf.write("Case #"+str(C)+": "+str(value[0]).zfill(4)+'\n')
  C+=1
  #printcounter()
  
outf.close()
inf.close()
