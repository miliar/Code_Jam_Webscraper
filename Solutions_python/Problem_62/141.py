#!/usr/bin/python
#
# Google CodeJam 2010
#  Round 1C
#  Problem A
#
# Author: David Volgyes
#

import sys,os,numpy
from sympy.geometry import *

def intersect(lines,i,j):
	if ((lines[i][0]-lines[j][0])*(lines[i][1]-lines[j][1]))<0:
		return True
	return False

T=int(sys.stdin.readline().strip())
for case in range(1,T+1):
	inputwords=sys.stdin.readline().strip().split()
	N=int(inputwords[0])
	lines=list()
	for i in range(0,N):
		l=list()
		inputwords=sys.stdin.readline().strip().split()
		l.append(int(inputwords[0]))
		l.append(int(inputwords[1]))
		lines.append(l)
	result=0
	for i in range(0,N):
		for j in range(i+1,N):
			if intersect(lines,i,j): result=result+1
	print("Case #%i: %s" % (case,result))
