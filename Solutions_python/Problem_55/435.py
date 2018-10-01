for c in range(1, input()+1):
	r, k, n = [int(d) for d in raw_input().split(' ')]
	g = [int(d) for d in raw_input().split(' ')]

	w = [0]*n
	ne = [-1]*n
	e = 0
	assert len(g) == n
	i = 0
	for cosa in range(0, r):
		if w[i] != 0:
			e += w[i]
			i = ne[i]
			continue
		if g[i] > k:
			continue


		s = 0
		j = i
		done = False
		while not done:
			v = g[j]
			if (s + v) <= k:
				s += v
				j += 1
				if j >= n:
					j = 0
				if j == i:
					done = True
			else:
				done = True

		w[i] = s
		ne[i] = j
		i = j
		e += s

	print "Case #%d: %d" % (c, e)

