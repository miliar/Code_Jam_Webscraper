TC = int(input())
for tc in range(TC):
	R, C = map(int, input().split())
	gd = [list(input()) for r in range(R)]
	fr = False
	for r in range(R):
		fst = False
		for c in range(C):
			if gd[r][c] != '?':
				fst = gd[r][c]
				break
		if fst != False:
			for c in range(C):
				if gd[r][c] == '?':
					gd[r][c] = fst
				else:
					fst = gd[r][c]
			if fr == False:
				fr = r
		elif r != 0:
			for c in range(C):
				gd[r][c] = gd[r-1][c]
	for r in range(R):
		if gd[r][0] == '?':
			for c in range(C):
				gd[r][c] = gd[fr][c]
	print('Case #%d:' % (tc+1))
	for r in range(R):
		print(''.join(gd[r]))
