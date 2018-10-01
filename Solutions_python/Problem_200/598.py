t = int(input())

for case in range(1,t+1):
	arr = [int(c) for c in input()]
	arr = arr[::-1]

	n = -1
	for i in range(len(arr)-1):
		if arr[i] < arr[i+1]:
			n = i
			arr[i+1] -= 1

	ans = arr[:n:-1] + [9]*(n+1) if n>=0 else arr[::-1]
	ans = ans[1:] if ans[0] == 0 else ans
	print('Case #%d: %s' % (case, ''.join(str(i) for i in ans)))
