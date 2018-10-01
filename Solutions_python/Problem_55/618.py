T = int(raw_input())

for case in range(T):
	R, k, N = map(int, raw_input().split())
	g = map(int, raw_input().split())
	
	nextG = 0
	totalRides = 0
	
	for ride in range(R):
		passengers = 0
		firstG = nextG
		# fill up the car
		while passengers + g[nextG] <= k:
			passengers += g[nextG]
			nextG = (nextG + 1) % len(g)
			if nextG == firstG:
				break
		totalRides += passengers
	
	print 'Case #' + str(case+1) + ": " + str(totalRides)

