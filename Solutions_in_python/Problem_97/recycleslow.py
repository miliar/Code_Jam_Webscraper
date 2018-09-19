#!/bin/python

def inRange(x, a, b):
	return a <= x and x <= b

def recyclables(x, a, b):
	cnt = 0
	s = str(x)
	for i in xrange(len(s)-1):
		s = s[1:] + s[0]
		if int(s) > x and len(str(x)) == len(str(int(s))) and inRange(int(s), a, b):
#			print x, s
			cnt += 1
	return cnt

f = open('in.txt', 'r')
out = open('out.txt', 'w')

N = int(f.readline())
for i in xrange(N):
	s = f.readline().split(" ")
	A = int(s[0])
	B = int(s[1])
	ctr = 0
	for x in xrange(A, B+1):
		ctr += recyclables(x, A, B)
	s = "Case #"+str(i+1)+": "+str(ctr)
	print s
	out.write(s+"\n")

