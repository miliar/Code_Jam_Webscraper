
T = int(input())
for t in range(1,T+1):
	cells,basins = {},{}
	H,W = (int(s) for s in input().split())
	
	for y in range(H):
		for x,s in enumerate(input().split()):
			cells[(x,y)] = int(s)
	
	def letter(k):
		if not k in basins:
			x,y = k
			neighbors = [c for c in [(x,y-1),(x-1,y),(x+1,y),(x,y+1)] if c in cells]
			lvl = min(cells[c] for c in neighbors)
			if cells[k] <= lvl:
				basins[k] = letter.next
				letter.next = chr(ord(letter.next) + 1)
			else:
				basins[k] = letter([n for n in neighbors if cells[n] == lvl][0])
		
		return basins[k]
	
	letter.next = 'a'
	print('Case #%s:' % t)
	if H == 1 and W == 1:
		print('a')
	else:
		print('\n'.join([' '.join([letter((x,y)) for x in range(W)]) for y in range(H)]))
