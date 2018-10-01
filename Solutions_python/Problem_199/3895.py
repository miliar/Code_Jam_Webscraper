M = {}
def flip(S):
	if S in M:
		return M[S]
	if S == '+' * len(S):
		return 0
	M[S] = float('inf')
	R = float('inf')
	for x in range(len(S) - K + 1):
		X = list(S)
		for y in range(x, x + K):
			X[y] = ['+', '-'][X[y] == '+']
		R = min(R, flip(''.join(X)) + 1)
	M[S] = R
	return R

T = int(input())
i = 0
while i < T:
	S, K = input().split()
	K = int(K)
	N = flip(S)
	if N == float('inf'):
		N = 'IMPOSSIBLE'
	print("Case #{}: {}".format(i + 1, N))
	M = {}
	i += 1
