T = int(raw_input())
for t in xrange(T):
	N, M = map(int, raw_input().split())
	grid = [map(int, raw_input().split()) for i in xrange(N)]
	rowmaxs = [max(grid[i]) for i in xrange(N)]
	colmaxs = [max((grid[i][j] for i in xrange(N))) for j in xrange(M)]
	simgrid = [[min(rowmaxs[i], colmaxs[j]) for j in xrange(M)] for i in xrange(N)]
	print 'Case #%d: %s' % (t+1, 'YES' if grid == simgrid else 'NO')
