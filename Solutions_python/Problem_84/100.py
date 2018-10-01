import psyco
import math
import sys

INPUT_FILENAME = "A-large"

sample = file("%s.in" % INPUT_FILENAME, "rb")
output = file("%s.out" % INPUT_FILENAME, "wb")

psyco.full()

def toOutput(line):
	print line
	output.write("%s\n" % line)

def solve(caseNumber, R, C, table):
	for i in xrange(R):
		for j in xrange(C):
			if table[i][j] == '#':
				if i == R - 1 or j == C - 1:
					toOutput("Case #%d:\nImpossible" % caseNumber)
					return
				if table[i + 1][j] != '#' or table[i][j + 1] != '#' or table[i + 1][j + 1] != '#':
					toOutput("Case #%d:\nImpossible" % caseNumber)
					return
				
				table[i][j] = '/'
				table[i + 1][j] = '\\'
				table[i][j + 1] = '\\'
				table[i + 1][j + 1] = '/'

	toOutput("Case #%d:" % caseNumber)

	for i in xrange(R):
		toOutput("".join(table[i]))

numberOfTestCases = int(sample.readline())
for i in xrange(1, numberOfTestCases + 1):
	R, C = map(int, sample.readline().split())

	table = [0] * R
	for j in xrange(R):
		table[j] = [0] * C

	for r in xrange(R):
		line = sample.readline().strip()
		for c in xrange(C):
			table[r][c] = line[c]

	solve(i, R, C, table)