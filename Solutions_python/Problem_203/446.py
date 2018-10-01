T = int(input())
for t in range(1,T+1):
	R,C = map(int,input().split())
	grid = [list(str(input())) for r in range(R)]
	answer = grid
	empty = []
	for r in range(R):
		fill = []
		for c in range(C):
			if grid[r][c] != '?':
				fill.append((grid[r][c],c))
		start = 0
		if len(fill) > 0:
			for d in fill:
				answer[r][start:d[1]+1] = [d[0]]*(d[1] - start + 1)
				start = d[1] + 1
			answer[r][start:] = [fill[-1][0]]*(C - start)	
		else:
			empty.append(r)
	empty_copy = [] 
	for e in empty:
		if e != 0 and e-1 not in empty_copy:
			answer[e] = answer[e-1]
		else:
			empty_copy.append(e)
	empty = empty_copy		
	empty.sort(reverse=True)		
	for e in empty:
		answer[e] = answer[e + 1]
	print('Case #{}:'.format(t))
	for row in answer:
		print(''.join(row))