from sys import stdin

for cs in xrange(1, 1+int(stdin.readline().strip())):
	vals = [int(z) for z in stdin.readline().split()]
	(n,s,p) = vals[0:3]
	ts = vals[3:]
	c = 0
	for t in ts:
		quo = t/3
		rem = t%3
		if 0==rem:
			#not-special-threshold & special-threshold
			nst=quo
			st=nst
			if 0 != t:
				st=nst+1
		if 1==rem:
			nst=quo+1
			st=nst
		if 2==rem:
			nst=quo+1
			st=quo+2
		
		if nst >= p:
			c += 1
		else:
			if st>=p and s>0:
				c += 1
				s -= 1
	print "Case #" + str(cs) + ": " + str(c)
  
