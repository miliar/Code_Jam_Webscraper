#Python

def checkWin(check, index):
	if check['O'] == 4 or (check['T'] == 1 and check['O'] == 3):
		print "Case #" + str(i+1) + ": O won"
		return 1
	if check['X'] == 4 or (check['T'] == 1 and check['X'] == 3):
		print "Case #" + str(i+1) + ": X won"
		return 1
	return 0

if __name__=="__main__":
	board = ["","","",""]
	N = int(raw_input())
	for i in range(N):
		for j in range(4):
			board[j] = raw_input()

		dotExist = 0
		r = 0
		#check horizontal
		for m in range(4):
			check = {'.':0,'T':0,'O':0,'X':0}
			if '.' in board[m]:
				dotExist = 1
			for c in board[m]:
				check[c] += 1
			r = checkWin(check, i)
			if r == 1:
				break
		#check vertical
		if r == 0:
			for m in range(4):
				check = {'.':0,'T':0,'O':0,'X':0}
				for n in range(4):
					check[board[n][m]] += 1
				if check['.'] > 0:
					dotExist = 1
				r = checkWin(check, i)
				if r == 1:
					break
		#check diagonal
		if r == 0:
			check = {'.':0,'T':0,'O':0,'X':0}
			for m in range(4):
				check[board[m][m]] += 1
			if check['.'] > 0:
				dotExist = 1
			r = checkWin(check, i)
		if r == 0:
			check = {'.':0,'T':0,'O':0,'X':0}
			for m in range(4):
				check[board[m][3-m]] += 1
			if check['.'] > 0:
				dotExist = 1
			r = checkWin(check, i)
		# check else
		if r == 0:
			if dotExist == 1:
				print "Case #" + str(i+1) + ": Game has not completed"
			else:
				print "Case #" + str(i+1) + ": Draw"

		if i < N-1:
			blank = raw_input()
