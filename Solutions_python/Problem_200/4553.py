for t in xrange(input()):
	for n in xrange(input(), 0, -1):
		if "".join(sorted(`n`))==`n`:
			print "Case #{t}: {n}".format(t=t+1, n=n)
			break
