#!/usr/bin/python

import foo
import math

def treesCoord(n, A, B, C, D, M, x0, y0):
	X = x0 
	Y = y0
	ret = []
	ret.append((X,Y))

	for i in range(1, n):
		X = (A * X + B) % M
		Y = (C * Y + D) % M
		ret.append((X,Y))

#	print ret
	return ret

# default for all problems
f = foo.getInputHandler()
out = foo.getOutputHandler()
cases = int(f.readline())

for run in range(1, cases+1):
	[n, A, B, C, D, x0, y0, M] = [int(x) for x in f.readline().split()]
	points = treesCoord(n, A, B, C, D, M, x0, y0)

	numOfTriangles = 0

	for i in range(len(points)):
		for j in range(i+1, len(points)):
			for k in range (j+1, len(points)):
				xc = (points[i][0] + points[j][0] + points[k][0]) / 3.0
				yc = (points[i][1] + points[j][1] + points[k][1]) / 3.0
				#print str(i) + ',' + str(j) + ',' + str(k) + ' = ' ,
				#print str(points[i][0]) + ',' + str(points[j][0]) + ',' + str(points[k][0]) + ' = ',
				#print str(xc) + ', ' + str(yc)
				if  xc == math.floor(xc) and yc == math.floor(yc):
					numOfTriangles += 1

	# answer
	out.write( "Case #" + str(run) + ": " + str(numOfTriangles) + "\n" )
