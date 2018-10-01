def change(ch):
	if ch == '+':
		return '-'
	return '+'

n = int(input())

for i in range(1, n + 1):
	s, k = input().split()
	k = int(k)
	s = list(s)

	ans = 0
	for j in range(len(s) - k + 1):
		if s[j] == '-':
			ans += 1
			for l in range(j, j + k):
				s[l] = change(s[l])
	
	print('Case #', i, ': ', ans if sum(map(lambda x: x == '+', s)) == len(s) else 'IMPOSSIBLE', sep='')
