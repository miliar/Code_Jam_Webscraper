t = int(input())

for case in range(1,t+1):
	s, k = input().split()
	k = int(k)
	arr = [1 if x == '+' else -1 for x in s]

	ans = 0
	for i in range(len(arr) - k + 1):
		if arr[i] == -1:
			for j in range(i, i+k):
				arr[j] *= -1
			ans += 1
	if any(x == -1 for x in arr[len(arr)-k+1:]):
		print('Case #%d: IMPOSSIBLE' % case)
	else:
		print('Case #%d: %d' % (case, ans))
