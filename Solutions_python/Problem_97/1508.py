#!/usr/bin/env python
import sys
indata = open(sys.argv[1], 'r').readlines()
indata = [x.strip() for x in indata]

def pairs(n, B):
	answer = set()
	nstr = str(n)
	for i in range(1, len(nstr)):
		trystr = nstr[i:len(nstr)] + nstr[0:i]
		if int(trystr) > n and int(trystr) <= B:
			answer.add(int(trystr))
	return len(answer)

tlines = int(indata[0])
for i in range(1, tlines+1):
	line = indata[i].split()
	assert len(line[0]) == len(line[1])
	A = int(line[0])
	B = int(line[1])
	answer = 0
	for n in range(A, B):
		answer += pairs(n, B)
	print "Case #%d: %d" % (i, answer)
