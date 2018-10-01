#!/usr/bin/python

N = int(raw_input())

matchstr = "welcome to code jam"
#matchstr = "abc"

for Case in xrange(1,N+1):
	
	stri = raw_input().strip()
	
	
	grid = [[0] * (len(stri) + 1 )
		for i in xrange(len(matchstr) + 1)]
	grid[0][0] = 0
	
	for i,j in enumerate(stri):
		if j == matchstr[0]:
			grid[0][i] = 1
		
	for i in xrange(1,len(matchstr) + 1):
		for j in xrange(1,len(stri) + 1):
			if (matchstr[i-1] == stri[j-1]):
				grid[i][j] = grid[i-1][j-1] + grid[i][j-1]
			else:
				grid[i][j] = grid[i][j-1]
			grid[i][j] %= 10000
	OP = str(grid[-1][-1])
	OP = ("0" * (4 - len(OP))) + OP
	'''
	print "  * " + (" ".join(stri))
	for i,j in zip("*" + matchstr,grid):
		print i, " ".join(str(k) for k in j)
	'''
	print "Case #%d: %s" % (Case, OP)
	