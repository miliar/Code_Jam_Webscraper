#!/usr/bin/python
#Filename:Tongues.py

import sys

def solveN(T,S,p,line):
	line.sort()
	line.reverse()
	cnt = 0
	scnt = 0
	for ti in line:
		if ti%3==0:
			a = ti/3
			if a>=p:
				cnt += 1
			elif scnt<S:
				a = (ti-3)/3
				if a>=0 and a<=10:
					scnt += 1
					if a+2>=p:
						cnt += 1
		elif ti%3==1:
			a = (ti-1)/3
			if a+1>=p:
				cnt += 1
			elif scnt<S:
				a = (ti-4)/3
				if a>=0 and a<=10:
					scnt += 1
					if a+2>=p:
						cnt += 1
		elif ti%3==2:
			a = (ti-2)/3
			if a+1>=p:
				cnt += 1
			elif scnt<S:
				a = (ti-2)/3
				if a>=0 and a<=10:
					scnt += 1
					if a+2>=p:
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

line = fin.readline().rstrip("\n")
testCaseNum = int(line)
for caseNum in xrange(1,testCaseNum+1):
	data = [int(val) for val in fin.readline().rstrip("\n").split()]
	T = data[0]
	S = data[1]
	p = data[2]
	ti = data[3:]
	an = solveN(T,S,p,ti)
	answer = "Case #%d: %d\n" %(caseNum,an)
	fout.write(answer)

fin.close()
fout.close()
