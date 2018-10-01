#!/usr/bin/env python

#  each row/col will be finally cut to one particular height that of the last lowest
#  as long as either row is unique "or" column is unique for each row and col it can be done

#if for every index i either row[i] or col[i] is unique you are ok
# for every row check the column entries lower than the highest entry
# they should be on a unique column
# for every col check the row entries lower than the highest entry
# they should be on a unique row
# if neither row-wise nor col-wise you are ok then NO

import math
import numpy as np

textfile = open("lawn.in");
lines = [line.strip() for line in textfile]
textfile.close()
textfile = open("lawn.out","w");

numCases = int( lines[0])
l = 1
for i in range(0,numCases,1):
	print lines[l].split()
	charlist = list(lines[l].split())
	N = int(charlist[0])
	M = int(charlist[1])
	#print "N = {n}".format(n=N)
	#print "M = {m}".format(m=M)
	lawn = np.empty((N,M))
	l = l + 1
	for n in range(0, N, 1): # n rows
		lawnlist = list(lines[l].split())
		#print lawnlist
		for m in range(0,M,1):
			#print m
			lawn[n][m] = int(lawnlist[m])
			#print lawn[n][m/2]
		l = l + 1
	
	# Now solve case i then proceed

	#print lawn
	if(N==1 or M == 1): # always possible
		textfile.write("Case #{case}: YES\n".format(case = i+1))
		#print "YES"
	else:
		rowWise = True
		colWise = True
		#check row wise stuff
		for r in range(0,N,1):
			# for each row, find the largest col element
			maxrow = -1
			for c in range(0,M,1):
				maxrow = max(maxrow,lawn[r][c])
			for c in range(0,M,1):
				if lawn[r][c] != maxrow:
					#it better be on it's own column
					for x in range (0,N,1):
						if lawn[x][c] != lawn[r][c]:
							rowWise = False
		#check col wise stuff		
		for c in range(0,M,1):
		# for each row, find the largest col element
			maxcol = -1
			for r in range(0,N,1):
				maxcol = max(maxcol,lawn[r][c])
				for r in range(0,N,1):
					if lawn[r][c] != maxcol:
						#it better be on it's own row
						for x in range (0,M,1):
							if lawn[r][x] != lawn[r][c]:
								colWise = False			
		if rowWise or colWise :
			textfile.write("Case #{case}: YES\n".format(case = i+1))
			#print "YES"
		else :
			textfile.write("Case #{case}: NO\n".format(case = i+1))
			#print "NO"


textfile.close()
