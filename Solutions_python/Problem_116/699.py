#!/usr/bin/python

import sys

def checkFull(case):
	for i in xrange(4):
		for j in xrange(4):
			if case[i][j]=='.':
				return False
	return True

def checkHorizs(case,player):
	for i in xrange(4):
		n=0
		for j in xrange(4):
			if case[i][j]==player:
				n=n+1
			if case[i][j]=='T':
				n=n+1
		if n==4:
			return True
	return False

def checkVerts(case,player):
	for i in xrange(4):
		n=0
		for j in xrange(4):
			if case[j][i]==player:
				n=n+1
			if case[j][i]=='T':
				n=n+1
		if n==4:
			return True
	return False

def checkDiags(case,player):
	n=0
	for i in xrange(4):
		if case[i][i]==player:
			n=n+1
		if case[i][i]=='T':
			n=n+1	
	if n==4:
		return True
	n=0
	for i in xrange(4):
		if case[i][3-i]==player:
			n=n+1
		if case[i][3-i]=='T':
			n=n+1
	if n==4:
		return True	
	return False

def processCase(case):
	# *** BEGIN CODE PROCESSING CASE ***

	if checkHorizs(case,'X'):
		return "X won"
	if checkVerts(case,'X'):
		return "X won"
	if checkDiags(case,'X'):
		return "X won"

	if checkHorizs(case,'O'):
		return "O won"
	if checkVerts(case,'O'):
		return "O won"
	if checkDiags(case,'O'):
		return "O won"		

	if checkFull(case):
		return "Draw"

	# *** END CODE PROCESSING CASE ***
	return "Game has not completed"

def readCase(case):

	caseInput=[]
	# *** BEGIN CODE READING CASE ***
	caseInput1=sys.stdin.readline()
	caseInput.append([])
	caseInput[0].append(caseInput1[0])
	caseInput[0].append(caseInput1[1])
	caseInput[0].append(caseInput1[2])
	caseInput[0].append(caseInput1[3])
	caseInput2=sys.stdin.readline()
	caseInput.append([])
	caseInput[1].append(caseInput2[0])
	caseInput[1].append(caseInput2[1])
	caseInput[1].append(caseInput2[2])
	caseInput[1].append(caseInput2[3])
	caseInput3=sys.stdin.readline()
	caseInput.append([])
	caseInput[2].append(caseInput3[0])
	caseInput[2].append(caseInput3[1])
	caseInput[2].append(caseInput3[2])
	caseInput[2].append(caseInput3[3])	
	caseInput4=sys.stdin.readline()
	sys.stdin.readline()
	caseInput.append([])
	caseInput[3].append(caseInput4[0])
	caseInput[3].append(caseInput4[1])
	caseInput[3].append(caseInput4[2])
	caseInput[3].append(caseInput4[3])	

	# *** END CODE READING CASE ***

	solution=processCase(caseInput)
	print "Case #"+str(case)+": "+solution

cases=int(sys.stdin.readline())

for case in range(cases):
	readCase(case+1)

