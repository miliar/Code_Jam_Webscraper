#!/usr/bin/python
import sys

if len(sys.argv) != 2:
	print 'Required: Filename'
	exit(2)

f = open(sys.argv[1], 'r')

total = 0;

testCasesTotal = int(f.readline())
testCaseCurrent = 1;

while testCaseCurrent <= testCasesTotal:
	result = 0
	ropes = [];
	ropesLeft = int(f.readline())
	while ropesLeft > 0:
		currentRope = map(int, f.readline().strip().split(' '));
		for rope in ropes:
			if (rope[0] > currentRope[0] and rope[1] < currentRope[1]) or (rope[0] < currentRope[0] and rope[1] > currentRope[1]) or (rope[0] == currentRope[0] or rope[1] == currentRope[1]):
				result += 1;
		ropes.append(currentRope)
		ropesLeft -= 1;
	print 'Case #%d: %d' % (testCaseCurrent, result);
	testCaseCurrent += 1;