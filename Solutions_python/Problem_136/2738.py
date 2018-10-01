T = input()
for i in xrange(T):
	prefix = "Case #%d:"%(i+1)
	res = 0.0
	S = 2.0
	C, F, X = [float(x) for x in raw_input().split()]
	while True:
		#X/S
		t1 = X/S
		t2 = C/S
		t3 = X/(S+F)
		if t1 > t2+t3:
			res+=t2
			S+=F
		else:
			res+=t1
			print prefix,res
			break


