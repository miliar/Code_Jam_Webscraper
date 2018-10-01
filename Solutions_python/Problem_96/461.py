#!/usr/bin/python

import sys

def canBeUsLeast(p,score):
	bestScore=score//3
	min=bestScore*3
	if (min<score):
		bestScore=bestScore+1
	if (bestScore>=p):
		return True
	return False

def canBeSLeast(p,score):
	bestScore=score//3
	min=bestScore*3
	remaining=score-min
	
	if score<=2:
		if remaining>=p:
			return True
		return False

	if remaining==0:
		if (bestScore+1)>=p:
			return True
		
	if remaining==1:
		if (bestScore+1)>=p:
			return True

	if remaining==2:
		if (bestScore+2)>=p:
			return True

	return False

def processCase(case):
	# *** BEGIN CODE PROCESSING CASE ***

	data=case.split()
	N=int(data[0])
	S=int(data[1])	
	p=int(data[2])
	googlers=data[3:N+3]

	candidates=0

	for employee in googlers:
		if canBeUsLeast(p,int(employee)):
			candidates=candidates+1
		elif (S>0) and (canBeSLeast(p,int(employee))):
			S=S-1
			candidates=candidates+1

	# *** END CODE PROCESSING CASE ***
	return candidates

def readCase(case):

	# *** BEGIN CODE READING CASE ***
	caseInput=sys.stdin.readline()
		
	# *** END CODE READING CASE ***

	solution=processCase(caseInput)
	print "Case #"+str(case)+": "+str(solution)

cases=int(sys.stdin.readline())

for case in range(cases):
	readCase(case+1)

