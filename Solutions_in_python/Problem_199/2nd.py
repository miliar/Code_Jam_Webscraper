t = int(raw_input())
for i in range(t):
	c, j = raw_input().split()
	j = int(j)
	c = '+' + c
	c = list(c)
	tmp = c[0]
	cnt = 0
	for k in range(1, len(c) - j + 1):
		if tmp != c[k]:
			for l in range(j):
				c[k + l] = '-' if c[k + l] == '+' else '+'
			cnt = cnt + 1
			tmp = c[k]
	try:
		n = c.index('-')
	except:
		n = -1
	if n == -1:
		print 'Case #' + str(i + 1) + ': ' + str(cnt)
	else:
		print 'Case #' + str(i + 1) + ': IMPOSSIBLE'
