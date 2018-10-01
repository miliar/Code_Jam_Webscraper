#!/usr/bin/python

import sys

def jumble(m):
	m = str(m)
	combinations = [m]
	for i in range(1, len(m)):
		combinations.append(m[-i:] + m[:-i])
	return combinations

infile = open("C-small-attempt0.in")

numcases = infile.readline()

for i in range(int(numcases)):
	print "Case #%i:" % (i + 1),
	a, b = infile.readline().strip().split(" ")
	b = int(b)
	count = 0
	for n in range(int(a), int(b)):
		nset = set(str(n))
		nstr = str(n)
		for m in range(n + 1, b + 1):
			if (nset == set(str(m))):
				if (nstr in jumble(m)):
					count += 1

	print count
