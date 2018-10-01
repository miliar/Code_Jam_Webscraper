for T in range(int(input())):
	D = int(input())
	P = list(map(int, input().split()))
	MinimumTime = max(P)
	Z = 2
	while Z < MinimumTime:
		MinimumTime = min(MinimumTime, sum([(x - 1) // Z for x in P]) + Z)
		Z += 1
	print('Case #%d: %s' % (T + 1, MinimumTime))