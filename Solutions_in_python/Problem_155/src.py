T = int(input())
for t in range(T):
	ans = 0
	S, a = input().split()
	S = int(S)
	cur = int(a[0])
	for j in range(1, S + 1):
		if cur < j:
			ans += max(0, j - cur)
			cur += max(0, j - cur)
		cur += int(a[j])
	print('Case #', t + 1, ': ', ans, sep='')