from copy import deepcopy

def rotate(board, N): ###
	board2 = deepcopy(board)
	for y, row in enumerate(board):
		for x, cell in enumerate(row):
			board2[N - 1 - y][x] = cell # [x][y]

	for x, _ in enumerate(board2):
		if board2[x].count('.') != N:
		#if bool(col.index('R')) or bool(col.index('B')):
		#if not all(map(lambda cell: cell == '.', col)):
			y = N-1
			while y > 0:
				if board2[x][y] == '.':
					board2[x].insert(0, board2[x].pop(y))
				else: y -= 1
				if all(map(lambda h: h == '.', board2[x][0:y+1])):
					break
			#y = N-1
			#if 'R' in board2[x]:
			#	if 'B' in board2[x]: y_min = min((board2[x].index('R'), board2[x].index('B')))
			#	else: y_min = board2[x].index('R')
			#else: y_min = board2[x].index('B')
			#while y > y_min:
			#	if board2[x][y] == '.':
			#		board2[x].insert(0, board2[x].pop(y))
			#	y -= 1
			#	if 'R' in board2[x]:
			#		if 'B' in board2[x]: y_min = min((board2[x].index('R'), board2[x].index('B')))
			#		else: y_min = board2[x].index('R')
			#	else: y_min = board2[x].index('B')
	#for w in board2:
	#	print w
	return board2

def join_k(board, K, N, case=None):
	def horizontal(c):
		for y in xrange(N):
			row = [board[x][y] for x in xrange(N)]
			if ''.join(row).count(c * K) > 0: return True
		return False
	def vertical(c):
		for col in board:
			if ''.join(col).count(c * K) > 0: return True
		return False
	def diagonal(c):
		for y in xrange(N):
			l = []
			x = 0
			y_ = y
			while 0 <= x < N and 0 <= y_ < N:
				l.append(board[x][y_])
				x += 1
				y_ -= 1
			#if case == 2: print l #####
			if ''.join(l).count(c * K) > 0: return True
		for x in xrange(N):
			l = []
			y = N-1
			while 0 <= x < N and 0 <= y < N:
				l.append(board[x][y])
				x += 1
				y -= 1
			#if case == 2: print l #####
			if ''.join(l).count(c * K) > 0: return True
		return False
	def diagonal2(c):
		for y in xrange(N):
			l = []
			x = N - 1
			y_ = y
			while 0 <= x < N and 0 <= y_ < N:
				l.append(board[x][y_])
				x -= 1
				y_ -= 1
			#if case == 2: print l #######
			if ''.join(l).count(c * K) > 0: return True
		for x in xrange(N):
			l = []
			y = N-1
			x_ = x
			while 0 <= y < N and 0 <= x_ < N:
				l.append(board[x_][y])
				x_ -= 1
				y -= 1
			#if case == 2: print l #####
			if ''.join(l).count(c * K) > 0: return True
		return False

	if horizontal('R') or vertical('R') or diagonal('R') or diagonal2('R'):
		if horizontal('B') or vertical('B') or diagonal('B') or diagonal2('B'):
			return 'Both'
		else:
			return 'Red'
	elif horizontal('B') or vertical('B') or diagonal('B') or diagonal2('B'):
		return 'Blue'
	else:
		return 'Neither'

T = int(raw_input())
for x in xrange(1, T + 1):
	N, K = map(int, raw_input().split(' '))
	board = [list(raw_input()) for _ in xrange(N)]
	y = join_k(rotate(board, N), K, N, x)
	print('Case #%d: %s' % (x, y))
