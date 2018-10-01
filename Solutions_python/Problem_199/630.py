Cases = int(input())
for Case in range(Cases):
	s, k = input().split()
	s = [1 if c=='-' else 0 for c in s]
	k = int(k)
	u = 0
	for i in range(len(s)-k+1):
		if s[i] == 1:
			for j in range(k):
				s[i+j] = 1-s[i+j]
			u += 1
	if sum(s) == 0:
		print('Case #%d: %d' % (Case+1, u))
	else:
		print('Case #%d: IMPOSSIBLE' % (Case+1))