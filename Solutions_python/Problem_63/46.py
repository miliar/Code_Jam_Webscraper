from __future__ import division
from math import ceil, log
import sys, operator, string

def choose(n,k):
	return reduce(lambda a,b: a*(n-b)/(b+1),xrange(k),1)

def PurgeZeros (TMZ):
	L = len(TMZ)
	i = 0
	while (i < L) and (TMZ[i] == 0):
		i = i + 1
	return TMZ[i:]
	

def Find (Vek,Ele):
	for i in range (len(Vek)):
		if Vek[i] == Ele:
			return i
	return -1

def InputLine():
	StrLine = sys.stdin.readline()
	L = [StrLine]
	LN = []
	n = 1
	i = Find (StrLine,' ')
	while i >= 0:
		L[n-1:] = [StrLine[:i], StrLine[i+1:]]
		StrLine = StrLine[i+1:]
		n = n+1
		i = Find (StrLine,' ')
	for Str in L:
		LN.append(int(Str))
	return LN


#MAIN FUNCTION
T = input()
for XX in range(1,T+1):
	LPC = InputLine()
	L = LPC[0]
	P = LPC[1]
	C = LPC[2]
	PL = ceil(P/L)
	Y2 = log (PL,C)
	Yfl = log (Y2,2)
	Y = int (ceil(Yfl))
	if Y < 0: Y = 0
		
	Str = "Case #" + str(XX) + ":"
	print Str, Y
	sys.stdout.flush()
