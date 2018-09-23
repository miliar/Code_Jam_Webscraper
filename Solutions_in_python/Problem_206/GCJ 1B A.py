#Google Code Jame 2017
#Round 2B
#Problem A. Steed 2: Cruise Control

T = int(raw_input())

for t in range(T):
	(D, N) = map(int,raw_input().split(" "))
	S = float(D*1000000)
	for n in range(N):
		(Ki, Si) = map(int,raw_input().split(" "))
		if float(Si*D)/(D-Ki) < S:
			S = float(Si*D)/(D-Ki)
	print "Case #{}: {:1.6f}".format(t+1, S)