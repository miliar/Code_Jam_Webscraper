def case(CN):
	A, N = map(long, raw_input().split(' '))
	M = map(int, raw_input().split(' '))
	
	M.sort()
	
	def solve(me, i, g):
		if i == N or g == N or me > M[-1]:
			return g
		
		if me > M[i]:
			return solve(me + M[i], i + 1, g)
		
		a = solve(me + me - 1, i, g + 1)
		
		if a < g + N - i:
			return a
		else:
			return g + N - i
	
	print 'Case #%s: %s' % (CN, solve(A, 0, 0))

if __name__ == '__main__':
	for i in xrange(int(raw_input())):
		case(i + 1)