N = int(raw_input())

for p in range(N):
	c, f, x = [float(x) for x in raw_input().split()]
	
	ps = 2
	sc = 0
	mn = 1e18
	while True:
		if x/ps+sc > mn: break
		mn = x/ps+sc
		sc = sc + c/ps
		ps = ps + f
	print "Case #%d: %.7f" % (p+1, mn)