#!/usr/bin/python

#creator = tbporter
#google code jam 2013
#param = input file, output file


import sys
import numpy as np

#returns false if it's an invalid lawn
def checkLawn(rng,grid):
	for i in rng:
		arr = np.where(grid==i)
		for j in range(len(arr[0])):
			#if both the row and column have values greater than itself(the val we are testing), it can't be done
			col = grid[:,arr[1][j]] > i
			row = grid[arr[0][j],:] > i
			if(np.sum(col)>0 and np.sum(row)>0):
				return 0
	return 1

fileIn = open(sys.argv[1],'r')
fileOut = open(sys.argv[2],'w')

num = int(fileIn.readline())

#try each test
for test in range(num):
	h,w = [int(x) for x in fileIn.readline().split()]
	lawn = []
	for i in range(h):
		for j in fileIn.readline().split():
			lawn.append(j)
	#shape the array into a grid
	grid = np.array(lawn)
	grid.shape = (h, w)

	#now get a set for each value to test on
	lawn.sort()
	rng = set(lawn)
	rng.remove(lawn.pop())#a waste to check the greatest number
	if(checkLawn(rng,grid)==1):
		fileOut.write("Case #"+str(test+1)+": YES\n")
	else:
		fileOut.write("Case #"+str(test+1)+": NO\n")