import itertools
f = open("C-small-attempt1.in")
T = int(f.readline().strip())
for i in range(1,T+1):
	g = []
	gs = []
	s = map(int, f.readline().strip().split())[1:]
	print "Case #" + str(i) + ":"
	not_found = True
	for i in range(1,19):
		if not_found:
			for j in itertools.combinations(s, i):
				sj = sum(j)
				while sj in gs:
					r_i = gs.index(sj)
					if sorted(j) != sorted(g[gs.index(sj)]):
						print " ".join(map(str, g[r_i]))
						print " ".join(map(str, j))
						not_found = False
						break
					gs = gs[:r_i] + gs[r_i+1:]
					g = g[:r_i] + g[r_i+1:]
				g.append(j)
				gs.append(sj)
				if not not_found:
					break
	if not_found:
		print " Impossible"