for p in xrange(input()):
	m, n = raw_input().split()
	m = int(m)
	tot = int(n[0])
	count = 0
	for i in xrange(1, m+1):
		if n[i] == '0' : continue
		if i > tot:
			count += (i - tot)
			tot += (i - tot)
		tot += int(n[i])
	print "Case #"+str(p+1)+": " + str(count)