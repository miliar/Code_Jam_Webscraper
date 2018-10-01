d = 'welcome to code jam'
xn = len(d)+1
n = int(raw_input())
for loop in xrange(n):
	s = raw_input()
	yn = len(s)
	v = [0] * xn
	v[0] = 1
	for c in s:
		nv = [0] * xn
		for i, q in enumerate(d):
			if c == q:
				nv[i+1] += v[i]
		for i in xrange(xn):
			v[i] += nv[i]
			v[i] = v[i] % 10000
	print 'Case #%d: %04d' % (loop+1,v[-1])



		

