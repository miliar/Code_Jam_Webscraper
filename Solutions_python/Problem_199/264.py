for i in range(int(input())):
	ps, ks = input().split()
	p = [0 if ch == "-" else 1 for ch in ps]
	k = int(ks)
	c = 0
	for j in range(len(p) - k + 1):
		if not p[j]:
			c += 1
			for l in range(k):
				p[j + l] = 1 - p[j + l]
	if all(p[j] for j in range(len(p) - k + 1, len(p))):
		print("Case #%d: %d" % (i + 1, c))
	else:
		print("Case #%d: IMPOSSIBLE" % (i + 1))
		