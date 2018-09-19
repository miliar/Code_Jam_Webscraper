#!/bin/python
import sys

fileName = sys.argv[1]

inputFile = open(fileName, 'r')
outputFile = open(fileName.strip('.in')+'.out', 'w')

numOfTestCases = int(inputFile.readline().strip())
for testid in xrange(numOfTestCases):
	line = inputFile.readline().strip()
	(R, C) = line.split()
	R = int(R)
	C = int(C)
	M = []
	resultPossible = True
	for i in xrange(R):
		M.append([])
		line = inputFile.readline().strip()
		for j in xrange(C):
			M[i].append(line[j])
	for i in xrange(R-1):
		for j in xrange(C-1):
			if (M[i][j] == '#' and M[i+1][j] == '#' and M[i][j+1] == '#' and M[i+1][j+1] == '#'):
				M[i][j] = '/'
				M[i+1][j+1] = '/'
				M[i+1][j] = '\\'
				M[i][j+1] = '\\'
	for i in xrange(R):
		for j in xrange(C):
			if M[i][j] == '#':
				resultPossible = False
	outputFile.write('Case #'+str(testid+1)+': ')
	if i != (numOfTestCases - 1):
		outputFile.write('\n')
	if not resultPossible :
		outputFile.write('Impossible\n')
	else:
		for i in xrange(R):
			for j in xrange(C):
				outputFile.write(M[i][j])
			outputFile.write('\n')
inputFile.close()
outputFile.close()