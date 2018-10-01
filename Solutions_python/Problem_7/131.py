#!/usr/bin/python

import sys
import string

from sets import Set

def findTrees(x0, y0, A, B, C, D, n, M):

	treeSet = Set([]) 
	trees = []

	X = x0
	Y = y0
	#print str(X) + "," + str(Y)
	treeSet.add((X, Y))
	for i in range(1, n):
		X = (A * X + B) % M
		Y = (C * Y + D) % M
		#print str(X) + "," + str(Y)
		treeSet.add((X, Y))

	#print treeSet
	
	# convert set of unique intersections into a list
	for i in range(0, len(treeSet)):
		trees.append(treeSet.pop())
			
	#print trees
	
	return trees
	
def findCenter(x1, y1, x2, y2, x3, y3):

	xc = (x1 + x2 + x3) % 3
	yc = (y1 + y2 + y3) % 3
	
	return(xc, yc)

def findTriangles(trees):

	count = 0
	for i in range(0, len(trees)):
		for j in range(i+1, len(trees)):
			for k in range(j+1, len(trees)):
			
				x1 = trees[i][0]
				y1 = trees[i][1]
				
				x2 = trees[j][0]
				y2 = trees[j][1]
				
				x3 = trees[k][0]
				y3 = trees[k][1]
				
				(xc, yc) = findCenter(x1, y1, x2, y2, x3, y3)
				#print "Checking: xc = " + str(xc) + ", yc = " + str(yc)
				if xc == 0 and yc == 0:
					count = count + 1

	return count

# usage: problem <input file> <output file>
if len(sys.argv) != 3:
	print "usage: problem <input file> <output file>"
	sys.exit()

inputfile = sys.argv[1]
outputfile = sys.argv[2]

# open the input file and read in the contents
infile = open(inputfile, "r")
outfile = open(outputfile, "w")

# read in the number of test cases
N = int(infile.readline())
print "The number of test cases is: " + str(N)

curCase = 1
for i in xrange(1, N+1):

	print "Test Case: " + str(curCase)
	trees = []
	
	line = infile.readline()
	items = line.split(' ')

	n = int(items[0])
	A = int(items[1])
	B = int(items[2])
	C = int(items[3])
	D = int(items[4])
	x0 = int(items[5])
	y0 = int(items[6])
	M = int(items[7])
	
	trees = findTrees(x0, y0, A, B, C, D, n, M)
	#print trees
	
	count = findTriangles(trees)
	print "Case " + str(curCase) + ": " + str(count)
	
	outfile.write("Case #%d: %d\r\n" % (curCase, count))
	
	curCase = curCase + 1
	

infile.close()
outfile.close()