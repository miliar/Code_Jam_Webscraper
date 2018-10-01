for t in range(input()):
	b,n = map(int,raw_input().split())
	m = map(int,raw_input().split())
	for i in range(10):
		m = m+m
	def solve(res):
		O=1
		U=10**30
		while O<=U:
			M=(O+U)/2
			D=0
			for i in range(res):
				D += (M+m[i]-1)/m[i]
			for i in range(res,b):
				D += (M-1+m[i]-1)/m[i]
			if D < n :
				O = M+1
			else:
				U = M-1
		return U+1
	res = [ 10**15, b+1 ]
	for ans in range(1,b+1):
		x = solve(ans)
		if res[0] > x :
			res[0] = x
			res[1] = ans
	print 'Case #%d: %d' % ( t+1, res[1] )