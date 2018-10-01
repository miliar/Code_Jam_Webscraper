T = int(input())

def check(n):
	return ''.join(sorted(str(n))) == str(n)

def solve1(N):
	for i in range(N, 0, -1):
		if check(i):
			return i
	return -1

def solve2(N):
	a = [int(x) for x in str(N)]
	for i in range(len(a) - 1):
		if a[i] > a[i + 1]:
			j = i
			while j >= 0 and a[j] == a[i]:
				j -= 1
			j += 1
			a[j] -= 1

			a[j+1:] = [9] * len(a[j+1:])
			ans = ''.join(map(str, a))
			return int(ans)
	return N



for t in range(1, T + 1):
	N = int(input())
	ans = solve2(N)
	print("Case #%d: %d" % (t, ans))