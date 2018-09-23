t = int(input())
for tt in range(1, t + 1):
	data = input().rstrip().split()
	s, k = list(data[0]), int(data[1])
	flips, l = 0, len(s)
	for i in range(l):
		if s[i] == '-':
			if l - i >= k:
				flips += 1
				for j in range(i, i + k):
					s[j] = '+' if s[j] == '-' else '-'
			else:
				flips = None
				break
	print("Case #%d: %s" % (tt, 'IMPOSSIBLE' if flips is None else str(flips)))
