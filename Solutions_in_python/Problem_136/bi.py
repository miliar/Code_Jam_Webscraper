import sys
def cookie(C, F, X, R, time, add=0):
	while X/R >= (C/R + X/(R+F)):	
		(R, time, add) = (R+F, time, add + time + C/R)
	return add + time + X/R
sys.setrecursionlimit(3000)
with open("B-large.in", "r") as infile:
	cases = int(infile.readline())
	for casenum in xrange(cases):
		time = 0
		(C, F, X) = [float(i) for i in infile.readline().split()]
		
		time += cookie(C, F, X, 2, time)
		cstring = str(time)
			
		print "Case #%s: %s"%(casenum + 1, cstring)
				
		