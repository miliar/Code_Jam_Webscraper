for t in range(input()):
	input()
	C = map(int,raw_input().split())
	n = 0
	for i in range(len(C)):
		if C[i]!=i+1:
			n += 1
	print "Case #%s: %s" % (t+1,n)
