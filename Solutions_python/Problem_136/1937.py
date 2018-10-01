T = input()

for t in range(T):
	C, F, X = map(float, raw_input().split())
	rate = 2
	time = 0

	while True:
		if X/rate > (C/rate + X/(rate+F)):
			time += C/rate
			rate += F
		else:
			time += X/rate
			break

	print "Case #%d: %f" % (t+1, time)