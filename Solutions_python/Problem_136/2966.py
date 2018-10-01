import sys
T = int(next(sys.stdin))

hit = lambda C, F, X, P: C/P+X/(P+F) < X/P

for x in range(T):
	P = 2
	C, F, X = map(float, next(sys.stdin).split())
	time = 0
	while True:
		if hit(C, F, X, P):
			time += C/P
			P += F
		else:
			print("Case #%s: %s" % (x+1, time + X/P))
			break
