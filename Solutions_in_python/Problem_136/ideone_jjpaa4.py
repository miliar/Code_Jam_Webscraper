def timeReq(C,F,X):
	time = 0
	totCookies = 0
	rate = 2.0
	while True:
		if X/rate > C/rate + X/(rate+F):
			time += C/rate
			rate += F
		else:
			time += X/rate
			break
	return time

t = int(raw_input())
for i in range(1,t+1):
	C,F,X = raw_input().split()
	C = float(C)
	X = float(X)
	F = float(F)
	time = timeReq(C,F,X)
	print "Case #{0}: {1}".format(i,time)