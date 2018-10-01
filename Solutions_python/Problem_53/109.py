t = int(raw_input())
for i in xrange(t):
	n, k = map(int,raw_input().split())
	print "Case #%d: %s" % ((i+1), "ON" if (k%(1<<n) == (1<<n) - 1) else "OFF")
