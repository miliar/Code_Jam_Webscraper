def calc(C, F, X, P):
	Y = X-C
	t1 = Y/P
	t2 = X/(P+F)
	if (t1 < t2): return t1
	else: return False
	
T = int(raw_input())
for t in range(1, T+1):
	line = raw_input().split()
	C = float(line[0])
	F = float(line[1])
	X = float(line[2])
	P = 2.0
	ans = False
	time = 0.0
	while (ans == False):
		time += C/P
		ans = calc(C, F, X, P)
		P += F
	time += ans
	print "Case #%d: %.7f"%(t, time)

