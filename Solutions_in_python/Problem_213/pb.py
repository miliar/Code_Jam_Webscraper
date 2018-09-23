t = int(input())

def check(arr_in, k):
	arr = list(arr_in)
	p = 0
	cnt = 0
	for i in range(len(arr)):
		while arr[i] > k and p < i:
			tmp = min(k-arr[p], arr[i]-k)
			arr[i] -= tmp
			arr[p] += tmp
			cnt += tmp
			while p < i and arr[p] == k:
				p += 1
		if p == i and arr[i] > k:
			return False, cnt
	return True, cnt

for case in range(1,t+1):
	n, c, m = [int(x) for x in input().split()]
	arr_n = [0 for i in range(n)]
	arr_c = [0 for i in range(c)]
	for i in range(m):
		p, b = [int(x) for x in input().split()]
		p -= 1
		b -= 1
		arr_c[b] += 1
		arr_n[p] += 1
	l = max(x for x in arr_c) - 1
	r = m
	while l < r-1:
		mid = (l + r) // 2
		if check(arr_n, mid)[0]:
			r = mid
		else:
			l = mid
	print("Case #%d: %d %d" % (case, r, check(arr_n, r)[1]))