from heapq import *

T = int(raw_input())
for I in range(T):
	N, K = raw_input().split()
	N, K = int(N), int(K)

	H = [-N-1]
	for i in range(K):
		curr = heappop(H)
		res = (curr/2, curr - curr/2)
		if res[0] == 1 and res[1] == 1:
			break
		heappush(H, res[0])
		heappush(H, res[1])
	
	print("Case #%d: %d %d" % (I+1, -1-res[0], -1-res[1]))
		
		