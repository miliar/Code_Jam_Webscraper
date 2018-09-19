#!/usr/bin/python
import sys, math

if len(sys.argv) != 2:
	print 'Required: Filename'
	exit(2)

f = open(sys.argv[1], 'r')

def solve(l, p, c):
	size, tests = 0, 0;
	a = l * c;
	while a < p:
		size += 1;
		a *= c;

	while size > 0:
		if size % 2 == 1:
			size -= 1
		size /= 2;
		tests += 1;

	return tests

testCasesTotal = int(f.readline())
testCaseCurrent = 1;

while testCaseCurrent <= testCasesTotal:
	input = map(int, f.readline().strip().split(' '));
	print 'Case #%d: %d' % (testCaseCurrent, solve(input[0], input[1], input[2]));
	testCaseCurrent += 1;