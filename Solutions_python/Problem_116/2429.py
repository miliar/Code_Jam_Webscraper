import collections 
def show(lst):
	for i in lst:
		print i

def process(board):
	tmp = horz(board)
	if (tmp == None):
		tmp = horz(map(list, zip(*board)))
	if (tmp == None):
		tmp = diag(board)
	if (tmp == None):
		if (dots(board)):
			return "Game has not completed"
		return "Draw"
	return tmp

def dots(board):
	n = collections.defaultdict(int)
	for i in board:
		for j in i:
			n[j] += 1
	return n['.'] > 0

def diag(board):
	n = len(board)
	collect = []
	for i in range(n):
		collect.append(board[i][i])
	tmp = count(collect)
	if (tmp == None):
		collect = []
		for i in range(n):
			collect.append(board[(n-1)-i][i])
		tmp = count(collect)
	return tmp

	



def horz(board):
	ans = None
	for row in board:
		if (ans == None):
			ans = count(row)
	return ans






def count(lst):
	n = collections.defaultdict(int)
	for i in range(len(lst)):
		n[lst[i]] += 1
	if n['.'] == 0:
		main = max(n['X'], n['O'])
		T = n['T']
		if main == 4 or (main == 3 and T == 1):
			if n['X'] > n['O']: 
				team = 'X'
			else:
				team = 'O'
			return team + " won"
		return None


# T, X, O, .
	

lines = [line.strip() for line in open('input.txt')]

n = int(lines[0]);
counter = 1
for i in range(n):
	board = []
	for j in range(4):
		board.append(lines[counter])
		counter += 1
	counter += 1
	print "Case #" + str(i+1) + ": " + process(board)




