# Qualification Round : Problem B

import sys
import os
import math

def ReadInput(filename):
	f = open(filename,'r')

	count = int(f.readline())

	ranges = []

	for i in range(count):
		temp = f.readline()
		if len(temp) == 0:
			break
		ranges.append(temp.strip().split())

	f.close()

	return ranges

def IsFair(x):
	s = str(x)
	l = len(s)
	fair = 0
	if len(s) % 2 != 0 or len(s) == 2:
		fair = 1
		for i in range(l/2):
			if s[i] != s[l-i-1]:
				fair = 0
	return fair

def CountFairAndSquare(a,b):
	count = 0
	for i in range(a,b+1):
		x = math.sqrt(i)
		if x == int(x):
			count += IsFair(i) & IsFair(int(x))
	return count

if len(sys.argv) < 3:
	sys.exit('    usage: <input> <output>')

filename = sys.argv[1]
outputFile = sys.argv[2]
f = open(outputFile,'w')

ranges = ReadInput(filename)

for i in range(len(ranges)):
	f.write("Case #%d: %d\n" % (i+1, CountFairAndSquare(int(ranges[i][0]),int(ranges[i][1]))))

f.close()