TC = int(input())
for tc in range(TC):
	D, N = map(int, input().split())
	C = 1e100
	for n in range(N):
		k, s = map(float, input().split())
		t = (D-k)/s
		C = min(C, D/t)
	print("Case #%d: %.10f" % (tc+1, C))
