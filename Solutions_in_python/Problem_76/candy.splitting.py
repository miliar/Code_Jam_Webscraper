#!/usr/bin/python

import sys
from math import pow

def convert(numbers):
	converted = []
	for i in range(len(numbers)):
		currnum = numbers[i]
		current = []
		for j in range(20):
			current.append(0)
		for j in range(20):
			if currnum % 2 != 0:
				currnum = (currnum - 1) / 2
				current[-(j + 1)] = 1
			else:
				currnum = currnum / 2
			if currnum == 0:
				break

		converted.append(current)

#	for conv in converted:
#		print conv
	return converted


def isGood(converted):
	for i in range(20):
		curr = 0
		for num in converted:
			curr += num[i]
		if curr % 2 != 0:
			return False
	
	return True


def solve(cases):
	sols = []

	for case in cases:
		if isGood(convert(case[0])):
			sols.append(str(case[1]))
		else:
			sols.append("NO")
	
	return sols


f = open(sys.argv[1],'r')
testCount = int(f.readline().strip('\n'))
#print testCount
cases = []
for i in range(testCount):
	f.readline()
	line = map(int,f.readline().strip('\n').split(' '))	
	case = (line,sum(line) - min(line))
	cases.append(case)

#for case in cases:
#	print case
solution = solve(cases)

for i in range(len(solution)):
	print "Case #" + str(i + 1) + ": " + solution[i]
