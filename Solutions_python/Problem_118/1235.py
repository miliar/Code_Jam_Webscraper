import sys
import math

def solve(a, b):
	c=0
	for x in range(a,b+1):
		s = str(x)
		sq = int(math.sqrt(x))
		sqs = str(sq)
		if (s == s[::-1] and sq*sq == x and sqs==sqs[::-1]):
			#print s
			c = c+1
	return c

N = int(sys.stdin.readline().strip())

for t in range(N):
	l = sys.stdin.readline().strip().split(" ")
	print "Case #{0}: {1}".format(t+1, solve(int(l[0]),int(l[1])))