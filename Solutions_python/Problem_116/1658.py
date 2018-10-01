def check(s):
	if s == 'XXXX': return 'X won'
	if s == 'OOOO': return 'O won'
	if s.count('O') == 3 and 'T' in s: return 'O won'
	if s.count('X') == 3 and 'T' in s: return 'X won'
	return None

def solve(board):
	for x in board:
		if check(x): return check(x)

	for x in xrange(4):
		s = ''.join(board)[x::4]
		if check(s): return check(s)

	ds = ''.join([board[x][x] for x in xrange(4)])
	if check(ds): return check(ds)
	ds = ''.join([board[x][3-x] for x in xrange(4)])
	if check(ds): return check(ds)

	if not ''.join(board).count('.'): return "Draw"
	return 'Game has not completed'

T = input()
for tc in xrange(T):
	
	board = []
	for _ in xrange(4):
		board += [raw_input()]
	try:
		raw_input()
	except:0

	print 'Case #%d: %s' % (tc+1, solve(board))

	