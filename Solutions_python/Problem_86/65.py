import sys, string
import itertools

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

T = int(sys.stdin.readline())

def har(i,notes):
	for n in notes:
		if n % i != 0 and i % n != 0:
			return 0
	return 1

for t in range(T):
	N,L,H = readlist()
	notes = readlist()
	
	print >> sys.stderr, N,L,H,notes
	ans = "NO"
	for i in range(L,H+1):
		if har(i,notes):
			ans = str(i)
			break
	print "Case #%d: %s" % (t+1, ans)
