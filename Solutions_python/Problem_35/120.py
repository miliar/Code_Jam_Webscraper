

def Solve(map, H, W):
	mark = ['a']
	result = [[None] * W for i in range(H)]
	
	def NewMark():
		m = mark[0]
		mark[0] = chr(ord(m) + 1)
		return m
		
	def GetMark(i, j):
		if result[i][j] != None:
			return result[i][j]
	
		coords =  [(i+ii, j+jj) for jj, ii in [(0, -1), (-1, 0), (+1, 0), (0, +1)]] #ii, jj are swapped, yes.
		coords =  [(iii, jjj) for iii, jjj in coords if (0 <=iii < H) and (0 <= jjj < W)]
		if len(coords) == 0:
			next_coord = None
		else:
			next_coord = min(coords, key = lambda (iii, jjj) : map[iii][jjj])
			
		if next_coord == None:
			r = NewMark()
		else:
			next_val = map[next_coord[0]][next_coord[1]] 
			if next_val >= map[i][j]:
				r = NewMark()
			else:
				r = GetMark(*next_coord)
		result[i][j] = r
		return r
			
	for i in range(H):
		for j in range(W):
			print GetMark(i, j),
		print

T = int(raw_input())
for i in range(1, T+1):
	print 'Case #%i:' % i
	H, W = map(int, raw_input().split())
	map_ = [map(int, raw_input().split()) for i in range(H)]
	assert all(len(row) == W for row in map_)
	Solve(map_, H, W)