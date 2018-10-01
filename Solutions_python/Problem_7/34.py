#!/usr/bin/env python

import sys
import math

def compute_trees(n , A, B, C, D, x0, y0, M):

	ans = [(x0, y0)]
	X, Y = x0, y0
	
	for i in range(1,n):
		X = (A*X+B)%M
		Y = (C*Y+D)%M
		ans.append((X,Y))
		
	return ans
	
def count_triangles(trees):

	numtrees = len(trees)
	count = 0
	
	for i in range(numtrees):
		for j in range(i+1, numtrees):
			for k in range(j+1, numtrees):
				#print '%s, %s, %s' % (i,j,k)
				x = float((trees[i][0] + trees[j][0] + trees[k][0])) / 3
				y = float((trees[i][1] + trees[j][1] + trees[k][1])) / 3
				if (x == int(x) and y == int(y)):
					count = count + 1
	
	return count
	
	
if __name__ == '__main__':

	inp = open(sys.argv[1])
	op = open(sys.argv[2], 'w')
	
	cases = int(inp.readline()[:-1])
	
	for i in range(1, cases+1):
	
		curcase = inp.readline()[:-1]
		b = curcase.split()
		c = len(b)
		for j in range(c):
			b[j] = int(b[j])
			
		d = count_triangles(compute_trees(*b))
		
		op.write('Case #%s: %s\n' % (i, d))
		
	inp.close()
	op.close()

	
