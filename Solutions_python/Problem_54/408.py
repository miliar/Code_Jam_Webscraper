#!/usr/bin/python3
#
# Google CodeJam 2010
# Qualification Round
#  Problem B
#
# Author: David Volgyes
#

import sys

def gcd(a, b):
	while b != 0:
		(a, b) = (b, a%b)
	return a

def calcT(diffs):
	minT=diffs[0]
	for i in range(0,len(diffs)):
		minT=gcd(diffs[i],minT)
	return minT

def solve(N,ti):
	ti.sort()
	diffs=[]
	minimum=ti[0]
	for i in range(1,len(ti)):
		diffs.append(ti[i]-minimum)
	diffs.sort()
	T=calcT(diffs)
	if ti[-1]%T==0: return 0
	return T-(ti[-1] % T)

T=int(sys.stdin.readline())

for case in range(1,T+1):
	inputwords=sys.stdin.readline().strip().split()
	N=int(inputwords[0])
	ti=[]
	for i in range(1,len(inputwords)):
		ti.append(int(inputwords[i].strip()))
	print("Case #%i: %s" % (case,solve(N,ti)))