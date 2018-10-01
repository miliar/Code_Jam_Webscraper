import sys
import math

TT = int(sys.stdin.readline())

for T in xrange(1,TT+1):
	ar = map(int, sys.stdin.readline().split())
	A, N = ar[0], ar[1]
	V = map(int, sys.stdin.readline().split())
	V = sorted(V)
	while len(V) > 0 and V[0] < A:
		A += V[0]
		V = V[1:]
	if len(V) == 0:
		print "Case #%d: 0"%T
		continue
	elif A == 1:
		print "Case #%d: %d"%(T,len(V))
		continue
	ans = len(V)
	m = 0
	for i in range(len(V)):
		while A <= V[i]:
			A += A - 1
			m += 1
		ans = min(ans, m+len(V)-i-1)
		A += V[i]
	print "Case #%d: %d"%(T,ans)
