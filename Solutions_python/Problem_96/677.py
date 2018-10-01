t = input()
for i in range(t):
	print "Case #%d:" % (i+1),
	v = map(int, raw_input().split())
	n, s, p = v[:3]
	v = v[3:]
	tr = []
	for x in v:
		y = [x/3, x/3, x/3 + x%3]
		if y[2] == y[1]+2:
			y[2] -= 1
			y[1] += 1
		tr.append(y)
	tr2 = []
	ans = 0
	for x in tr:
		if x[2] >= p:
			ans += 1
		else:
			tr2.append(x)
	for x in tr2:
		if s > 0:
			if x[1] > 0:
				if x[1] != x[2]-1:
					x[2] += 1
					x[1] -= 1
					if x[2] >= p:
						ans += 1
						s -= 1
	print ans
