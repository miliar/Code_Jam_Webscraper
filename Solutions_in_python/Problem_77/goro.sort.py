#!/usr/bin/python

import sys

def cCount(random,ordered):
	total = 0
	for i in range(len(random)):
		if random[i] == ordered[i]:
			total += 1

	return total


def solve(cases):
	sols = []

	for case in cases:
		tmp = []
		for i in case:
			tmp.append(i)
		tmp.sort()
		correct = cCount(case,tmp)
		sols.append(str(len(case) - correct) + ".000000")

	return sols


f = open(sys.argv[1],'r')
caseCount = int(f.readline().strip('\n'))
#print caseCount
cases = []
for i in range(caseCount):
	f.readline()
	cases.append(map(int,f.readline().strip('\n').split(' ')))

#print cases
solution = solve(cases)

for i in range(len(solution)):
	print "Case #" + str(i + 1) + ": " + str(solution[i])
