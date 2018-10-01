from heapq import heappush, heappop

def solve(N, K): 
	# if K >= N/2+2: 
	#	return (0,0)

	segments = []
	heappush(segments, -N)

	for k in range(K-1): 
		maximum = -1* heappop(segments) 
		if maximum % 2 == 1: 
			heappush(segments, -1* int(maximum/2))
			heappush(segments, -1* int(maximum/2))
		else: 
			heappush(segments, -1* int(maximum/2))
			heappush(segments, -1* (int(maximum/2)-1))
	maximum = -1*heappop(segments)

	if maximum % 2 == 1:  
		return (maximum/2, maximum/2)
	else: 
		return (maximum/2, (maximum/2-1))

num_cases = int(raw_input()) 
for n in range(num_cases): 
	N,K = map(int, raw_input().split())
	soln = solve(N,K)
	print "Case #%d: %d %d" % (n+1, soln[0], soln[1])