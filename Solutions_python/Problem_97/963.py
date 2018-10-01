#!/usr/bin/python
#Filename:Tongues.py

import sys

def getLen(A):
	l = 0
	while(A>0):
		A = A/10
		l = l + 1
	return l

def solveN(A,B):
	cnt = 0
	l = getLen(A)
	for x in range(A,B+1):
		sx = "%d" %(x)
		trec = dict()
		for i in xrange(l):
			sx = sx[l-1]+sx[0:l-1]
			v = int(sx)
			if v>x and v<B+1:
				if sx not in trec:
					trec[sx]=v
				#	print x,sx
					cnt += 1
	return cnt


inname = "input.txt"
outname = "output.txt"
if len(sys.argv)>1:
	inname = sys.argv[1]
	outname = inname.rstrip(".in")
	outname = outname + ".out"
fin = open(inname,"r")
fout = open(outname,"w")

testCaseNum = int(fin.readline().rstrip("\n"))
for caseNum in xrange(1,testCaseNum+1):
	(A,B) = [int(val) for val in fin.readline().rstrip("\n").split()]
	cnt=solveN(A,B)
	answer = "Case #%d: %d\n" %(caseNum,cnt)
	fout.write(answer)

fin.close()
fout.close()
