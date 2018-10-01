#!/usr/bin/python2.5
import sys
import bisect
import math

inputName = "test.in" if (len(sys.argv) < 2) else sys.argv[1]
file = open(inputName, "r")

def readline(): return file.readline().strip(" \n")

for case in range(int(readline())) :
	n, A, B, C, D, X, Y, M = map(int, readline().split())
	
	#print (n, A, B, C, D, X, Y)
	
	ALL = [(X, Y)]

	for i in range(n - 1):
		X, Y = (A * X + B) % M, (C * Y + D) % M
		ALL.append((X, Y))
	
	ALL.sort()
	#print ALL
	res = 0
	
	for i in range(n):
		for j in range(i):
			for k in range(j):
				x1, y1 = ALL[i][0] + ALL[j][0] + ALL[k][0] , ALL[i][1] + ALL[j][1] + ALL[k][1]
				if (x1 %3 == 0 and y1 % 3 == 0):
						res+=1
				
	

		

	print "Case #%s: %s" % (case + 1, res)
	

	