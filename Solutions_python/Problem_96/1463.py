t = input()
for i in xrange(t):
	ln = map(int,raw_input().split())
	n = ln[0]
	s = ln[1]
	p = ln[2]
	ts = ln[3:]
	sol = 0

	for te in ts:

		div = te/3
		mod = te%3
		if div >= p:
			sol+=1
			continue
		if mod > 0 and div+1 >= p:
			sol+=1
			continue
		if div+2 >= p and s>0 and mod > 1 :
			s-=1
			sol+=1
			continue
		if div+1 >= p and s>0 and (mod>0 or div>0):
			s-=1
			sol+=1
			continue
	print "Case #%d: %d" % (i+1,sol)
