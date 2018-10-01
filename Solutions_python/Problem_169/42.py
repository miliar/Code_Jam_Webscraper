T = input()
for kase in xrange(1,T+1):
	N,V,X = raw_input().split()
	N = int(N)
	V,X = float(V),float(X)
	F = [map(float,raw_input().split()) for i in xrange(N)]
	if len(F) == 2:
		if (F[0][1] == X or F[1][1] == X):
			v = 0
			if F[0][1]==X:
				v+=F[0][0]
			if F[1][1]==X:
				v+=F[1][0]
			print "Case #%d: %.12lf"%(kase,V/v)
		elif (F[0][1] - X) * (F[1][1] - X) < 0:
			lo = 0.0
			hi = F[0][0]
			for i in xrange(100):
				myV = (lo + hi) / 2.0
				yourV = -myV * (F[0][1] - X) / (F[1][1] - X)
				if yourV > F[1][0]:
					hi = myV
				else: 
					lo = myV
			print "Case #%d: %.12f"%(kase,V/(myV+yourV))
		else:
			print "Case #%d: IMPOSSIBLE"%(kase,)

	else:
		if F[0][1] == X:
			print "Case #%d: %.12lf"%(kase,V/F[0][0])
		else:
			print "Case #%d: IMPOSSIBLE"%(kase,)
