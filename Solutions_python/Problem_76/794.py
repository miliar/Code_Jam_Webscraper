T = int( raw_input() )
for testCase in xrange( 1, T+1 ):
	N = int( raw_input() )
	A = [ int(x) for x in raw_input().strip().split() ]
	res = 0 
	for i in xrange(N): res ^= A[i]
	if res != 0:
		print "Case #" + str(testCase) + ": NO"
	else:
		print "Case #" + str(testCase) + ":", sum( A ) - min( A )