#!/usr/bin/env python
import sys, os
from numpy import *


ifile=open('A-small.in', 'r')
ofile=open('A-small.out','w')
output=''

lines = ifile.readlines()
T = int(lines[0])

def snapper(N,K):
	snappers=zeros(N,dtype=bool)
	powers=zeros(N,dtype=bool)
	powers[0]=True
	
	for i in range(0,K):
		for a in range(0,N):
			if (powers[a]):
				snappers[a] = not snappers[a]
		for a in range(1,N):
			if ((powers[a-1]) and (snappers[a-1])):
				powers[a]=True
			else:
				powers[a]=False
	#print snappers
	#print powers

				
	return snappers[N-1]*powers[N-1]

i=1
for line in lines[1:]:
	l=line.split()
	N = int(l[0])
	K = int(l[1])
	if (i<>1): output+='\n'
	output+=('Case #%d: ' % (i))
	if (snapper(N,K)): output+='ON'
	else:	output+='OFF'
	i+=1
	print snapper(N,K)
ofile.write(output)
ofile.close()
ifile.close()


