def get_trees(n, A, B, C, D, x0, y0, M):
	x = x0
	y = y0
	trees = [(x,y)]
	for i in range(1, n):
		x = (A * x + B) % M
		y = (C * y + D) % M
		trees.append((x, y))
	return trees
		
for case in range(input()):
	inp = tuple(map(int, raw_input().split()))
	t = apply(get_trees, inp)
		
	good = 0
	processed = {}
	n = inp[0]
	for i in range(n):
		for j in range(n):
			if j == i:
				continue
			for k in range(n):
				if k == i or k == j:
					continue
				key = tuple(sorted((i, j, k)))
				if processed.has_key(key):
					continue
				else:
					processed[key] = 0
					cx = t[i][0] + t[j][0] + t[k][0]
					cy = t[i][1] + t[j][1] + t[k][1]
					if cx % 3 != 0 or cy % 3 != 0:
						continue
					processed[key] = 1
					good += 1
				
	print "Case #%d: %d" % (case+1, good)