for C in xrange(1, input()+1):
	N, K = map(int, raw_input().split())
	
	if K%(2**N) == (2**N)-1:
		res = "ON"
	else:
		res = "OFF"
	print "Case #%d: %s" % (C, res)
