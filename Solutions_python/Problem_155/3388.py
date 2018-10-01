import sys
sys.stdin = open('gcj1.in', 'r')
sys.stdout = open('gcj1.out', 'wb')

for t in xrange(input()):
	S, k = raw_input().split()
	S = int(S)
	k = map(int, list(k))
	c = k[0]
	n = 0
	for i in xrange(1, len(k)):
		o = k[i]
		if i > (c + n):
			n += i-(c+n)
		c += o
	print "Case #%d: %d" % (t + 1, n)