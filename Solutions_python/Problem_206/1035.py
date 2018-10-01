T = int(input())
for cases in range(1, T+1):
	D, N = [int(x) for x in input().split()]
	fin = 0
	for horses in range(N):
		K, S = [int(x) for x in input().split()]
		fin = max(fin, (D - K) / S)
	ans = D / fin
	print(f'Case #{cases}: {round(D/fin, 6)}')
