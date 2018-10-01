base = set("Q W E R A S D F".split())

nc = input()
for ci in range(1, nc + 1):
	s = raw_input().split()
	i = 0
	n = int(s[i])
	i += 1
	c = {}
	for j in range(0, n):
		x, y = s[i + j][:2], s[i + j][-1]
		c[x] = c[x[::-1]] = y
	i += n
	n = int(s[i])
	i += 1
	d = set()
	for j in range(0, n):
		x = s[i + j][:2]
		d.update([x, x[::-1]])

	i += n
	n = int(s[i])
	i += 1
	e = s[i][:n]
	r = []
	for k in range(0, n):
		r += [e[k]]
		while len(r) > 1:
			t = r[-1] + r[-2]
			if t not in c: break
			del r[-1]
			r[-1] = c[t]
		found = False
		for i in range(0, len(r) - 1):
			if r[i] not in base: continue
			for j in range(i, len(r)):
				if r[j] not in base: continue
			if r[i] + r[j] in d:
				r = []
				found = True
				break
			if found: break

	print "Case #{0}: [{1}]".format(ci, ', '.join(r))
