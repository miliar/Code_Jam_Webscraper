#!/usr/bin/python

import sys

transformations=[]
opposites=[]
result=[]

def checkOpposites():
	global opposites
	global result
	for oppo in opposites:
		if result[-1]==oppo[0]:
			if oppo[1] in result:
				result=[]
				return
		if result[-1]==oppo[1]:
			if oppo[0] in result:
				result=[]
				return

def transform():
	global result
	global transformations
	element1=result.pop()
	element2=result.pop()
	for transf in transformations:
		if (element1==transf[0])and(element2==transf[1]):
			result.append(transf[2])
			return True
		if (element2==transf[0])and(element1==transf[1]):
			result.append(transf[2])
			return True
	result.append(element2)
	result.append(element1)
	return False

def processCase(case,invocation):
	global result
	char=0
	result.append(invocation[char])
	char=char+1
	for element in range(len(invocation)-1):
		result.append(invocation[char])
		char=char+1
		if len(result)==1:
			continue
		if not transform():
			checkOpposites()
			
	result_str = str(result).replace("'","")
	print "Case #"+str(case+1)+": "+result_str 

def readCase(case):
	caseInput=sys.stdin.readline()
	tokens=caseInput.split()
	tokens.reverse()
	numberOfTrans=int(tokens.pop())
	for t in range(numberOfTrans):
		transformations.append(tokens.pop())
	numberOfOppos=int(tokens.pop())
	for t in range(numberOfOppos):
		opposites.append(tokens.pop())
	tokens.pop() # skip number
	invocation=tokens.pop()
	processCase(case,invocation)

# AQUI EMPIEZA LA EJECUCION
cases=int(sys.stdin.readline())

for case in range(cases):
	readCase(case)
	transformations=[]
	opposites=[]
	result=[]
	

