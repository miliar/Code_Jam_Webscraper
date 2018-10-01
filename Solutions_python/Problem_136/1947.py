T = input()
# T = 1
# [raw_input() for i in xrange(3)]
for t in xrange(T):
	m = t+1
	C, F, X = [float(_) for _ in raw_input().split()]
	n = 0.0 #Seconds
	c = 0 #Cookies
	b = 2.0 #Rate
	while c < X:
		#If it is better to buy a farm, 
		# then the time it takes to get to the goal is less than
		# the time it takes to buy another one + get to the goal
		# print (X/(b+F)) + (C/b), X/b
		if (X/(b+F)) + (C/b) > X/b:
			n += X/b
			# print "STOP"
			break 
		a = C/b
		# print a
		c -= C
		c += a * b
		n += a
		b += F
		# print c, a, b, n
	print "Case #%d: %.7f" % (m, n)