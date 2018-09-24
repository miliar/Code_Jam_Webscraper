import sys
problemset = sys.argv[1]
inf = file('A-'+problemset+'.in')
outf = file('A-'+problemset+'.out','w')

N = int(inf.readline()) # Number of test cases
for testcase in xrange(N):
	S = int(inf.readline()) # Number of search engines
	E = {} # Search engines
	for x in xrange(S):
		E[inf.readline().strip()] = x
	Q = int(inf.readline()) # Number of queries
	D = [0]*Q # D - Actual queries
	for x in xrange(Q):
		D[x] = E[inf.readline().strip()]
		
	G = {} # Read
	A = 0 # Answer
	for x in xrange(Q-1,-1,-1):
		G[D[x]] = 1
		if len(G) == S:
			G = {D[x]:1}
			A += 1
	print >> outf, "Case #"+str(testcase+1)+": "+str(A)
