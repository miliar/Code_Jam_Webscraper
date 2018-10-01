#!/usr/bin/env python

result = []
m = 0
n = 0

def isNotDPI(num):
	return len(set(str(num))) != len(list(str(num)))

def getPairNumber(m, n):
	pairSet = set()
	if m == n:return 0
	for i in range(m, n+1):
		ilen = len(str(i))
		for j in range(1, ilen):
			num2 = i/(10**j) + i%(10**j)*(10**(ilen-j))
			if i < num2 and num2 >= m and num2 <= n:
				pairSet.add((i, num2))
	return len(pairSet)

linenum = raw_input()

for l in range(1, int(linenum)+1):
	line = raw_input()
	numbers = line.split()
	m = int(numbers[0])
	n = int(numbers[1])
	pairNumber = getPairNumber(m, n)
	result.append("Case #" + str(l) + ": " + str(pairNumber))

for str in result:
	print str
