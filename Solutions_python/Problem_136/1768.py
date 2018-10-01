def time_with_n_farms(C, F, X, n):
	if n==0:
		return X/2
	t = X/( 2+n*F)
	a= list(range(0,n))
	b = [1/(2+F*i) for i in a]
	return t+C*sum(b)
case_num = int(raw_input())
for i in xrange(1, case_num+1):
	print 'Case #%d:'%i,
	C, F, X = (float(x) for x in raw_input().split())
	min = X/2
	max_rounds = int(X/C) + 2
	for n in range(0,max_rounds):
		t_n = time_with_n_farms (C,F,X,n)
		if t_n < min:
			min = t_n
	print "%.7f" % min