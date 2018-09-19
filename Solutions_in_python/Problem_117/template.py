#!/usr/bin/python

import sys
from copy import deepcopy

def fillRight(case,rows,cols):
	for i in xrange(rows):
		maxi=case[i][0]
		for j in xrange(cols):
			if case[i][j]>maxi:
				maxi=case[i][j]
			case[i][j]=maxi

def fillLeft(case,rows,cols):
	for i in xrange(rows):
		maxi=case[i][cols-1]
		for j in reversed(xrange(cols)):
			if case[i][j]>maxi:
				maxi=case[i][j]
			case[i][j]=maxi

def fillUp(case,rows,cols):
	for j in xrange(cols):
		maxi=case[0][j]
		for i in xrange(rows):
			if case[i][j]>maxi:
				maxi=case[i][j]
			case[i][j]=maxi

def fillDown(case,rows,cols):
	for j in xrange(cols):
		maxi=case[rows-1][j]
		for i in reversed(xrange(rows)):
			if case[i][j]>maxi:
				maxi=case[i][j]
			case[i][j]=maxi			

def processCase(case,rows,cols):
	# *** BEGIN CODE PROCESSING CASE ***
	left=deepcopy(case)
	right=deepcopy(case)
	up=deepcopy(case)
	down=deepcopy(case)

	fillRight(right,rows,cols)
	fillLeft(left,rows,cols)
	fillUp(up,rows,cols)
	fillDown(down,rows,cols)

	for c in xrange(cols):
		for r in xrange(rows):
			if ((case[r][c]<right[r][c]) or (case[r][c]<left[r][c])) and ((case[r][c]<up[r][c]) or (case[r][c]<down[r][c])):
				return "NO"

	# *** END CODE PROCESSING CASE ***
	return "YES"

def readCase(case):

	caseTarget=[]
	# *** BEGIN CODE READING CASE ***
	caseInput=sys.stdin.readline()
	rows=int(caseInput.split()[0])
	cols=int(caseInput.split()[1])
		
	for r in xrange(rows):
		caseTarget.append([])
		caseInput=sys.stdin.readline()
		heights=caseInput.split()
		for el in heights:
			caseTarget[r].append(el)

	# *** END CODE READING CASE ***

	solution=processCase(caseTarget,rows,cols)
	print "Case #"+str(case)+": "+solution

cases=int(sys.stdin.readline())

for case in range(cases):
	readCase(case+1)

