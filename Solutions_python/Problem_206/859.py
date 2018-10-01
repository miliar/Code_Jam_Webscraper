'''input
3
2525 1
2400 5
300 2
120 60
60 90
100 2
80 100
70 10
'''
T = int(input())
for t in range(T):
	D, N = map(int, input().split())
	horses = []
	slowest = 0
	for n in range(N):
		K, S = map(int, input().split())

		dist = D - K
		slowest = max(dist/S, slowest)
		
	print('Case #{}: {:.6f}'.format(t + 1, D/slowest))
