from itertools import izip
t = int(raw_input())

for case in xrange(1,t+1):
	n = int(raw_input())
	
	vec1 = [int(i) for i in raw_input().split()]
	vec2 = [int(i) for i in raw_input().split()]
	
	vec1.sort()
	vec2.sort()
	vec2.reverse()
	
	msp = sum(i*j for i,j in izip(vec1,vec2))
	print "Case #%d: %d" % (case, msp)