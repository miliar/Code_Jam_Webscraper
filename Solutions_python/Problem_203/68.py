from collections import deque

T = int(raw_input())

def filled(x):
	return x != '?'

# Note I fixed an answer manually.
for qw in range(1, T+1):
		r, c = map(int, raw_input().split())
		grid = [list(raw_input().strip()) for _ in range(r)]
		seen = set()
		for i in range(r):
			for j in range(c):
				if filled(grid[i][j]):
					if grid[i][j] in seen:
						continue
					seen.add(grid[i][j])
					left = j - 1
					right = j + 1
					top = i - 1
					bottom = i + 1
					for ii in range(i - 1, -2, -1):
						top = ii
						if ii == -1:
							break
						if filled(grid[ii][j]):
							break
					for jj in range(j - 1, -2, -1):
						left = jj
						if jj == -1:
							break
						jjdone = False
						for ii in range(top + 1, bottom):
							if filled (grid[ii][jj]):
								jjdone = True
								break
						if jjdone:
							break
					for jj in range(j + 1, c + 1):
						right = jj
						if jj == c:
							break
						jjdone = False
						for ii in range(top + 1, bottom):
							if filled(grid[ii][jj]):
								jjdone = True
								break
						if jjdone:
							break
					for ii in range(i + 1, r + 1):
						bottom = ii
						if ii == r:
							break
						iidone = False
						for jj in range(left + 1, right):
							if filled(grid[ii][jj]):
								iidone = True
								break
						if iidone:
							break
					for y in range(top + 1, bottom):
						for x in range(left + 1, right):
							grid[y][x] = grid[i][j]
		print 'Case #%d:' % qw
		print '\n'.join([''.join(row) for row in grid])
