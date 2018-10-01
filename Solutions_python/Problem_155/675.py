def solve():
	n, a = raw_input().split()
	n = int(n)
	res = 0
	s = 0
	for i, x in enumerate(a):
		if res < i - s:
			res = i - s
		s += int(x)
	return res

for i in xrange(input()):
	print "Case #%d: %d" % (i + 1, solve())
