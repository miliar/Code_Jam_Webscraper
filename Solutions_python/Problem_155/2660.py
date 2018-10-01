#!/usr/bin/python

"""
Problem A. Standing Ovation
https://code.google.com/codejam/contest/6224486/dashboard#s=p0
"""

import sys

input_file = sys.argv[1]

def get_file_line(file):
	fd = open(file,'r')
	for line in fd:
		yield line.strip().split(' ')


def resolve_case(Smax,A):
	[friends, standing, k] = [0, 0, 0]
	while (standing < Smax):
		if k > standing:
			friends += (k - standing)
			standing = friends + sum(A[:k+1])
			k=standing
		else:
			standing = friends + sum(A[:k+1])
			k += 1
	return friends


file_line = get_file_line(input_file)
test_cases = int(file_line.next()[0])

for T in xrange(1,test_cases+1):
	[Smax, A] = file_line.next()
	friends = resolve_case(int(Smax),[int(x) for x in A])
	print("Case #%d: %d" % (T,friends))

