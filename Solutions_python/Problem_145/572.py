from fractions import gcd
import sys

f = open(sys.argv[1])
N = int(f.readline().rstrip())
for case in xrange(1,N+1):
	[p,q] = map(int, f.readline().rstrip().split("/"))
	count = 0
	#tmp = p
	while p < q:
		#tmp += tmp
		p += p
		count += 1
	diff = p - q
	g = gcd(diff, q)
	s_q = q/g
	print "Case #%s:" %(case),
	if (s_q & s_q-1 == 0): 
		print count	
	else:
		print 'impossible'
