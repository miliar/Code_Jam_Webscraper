#!/usr/bin/env python2.6

def solve(lines):
	lst = getList(lines)
	rslt = 0
	for i in range(len(lst)):
		pos = findFirstNotAbove(lst,i)
		if pos > i:
			lst = lst[0:i] + [lst[pos]] + lst[i:pos] + lst[pos+1:]
			rslt += (pos - i)
	return rslt

def findFirstNotAbove(lst, x):
	for i in range(x,len(lst)):
		if lst[i] <= x:
			return i

def getList(lines):
	rslt = []
	for line in lines:
		rslt.append(line.rfind("1"))
	return rslt

import sys
lines = sys.stdin.read().split("\n")
numTestCases = int(lines[0])
lines = lines[1:]
linenr = 0
for testCase in range(numTestCases):
	numLines = int(lines[linenr])
	caseLines = lines[linenr+1:linenr+1+numLines]
	linenr += numLines + 1
	answer = solve(caseLines)
	print "Case #%d: %d" % (testCase + 1, answer)
