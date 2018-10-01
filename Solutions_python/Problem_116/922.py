with open('input.txt', 'r') as inFile, open('output.txt', 'w') as outFile:
	
	n = int(inFile.readline())
	for i in range (n):
		board = []
		for j in range (4):
			board.append(list(inFile.readline()))
		isSolution = 0
		for j in range (4):
			if (((board[j][0] == 'T' or board[j][0] == 'O') and (board[j][1] == 'T' or board[j][1] == 'O') and (board[j][2] == 'T' or board[j][2] == 'O') and (board[j][3] == 'T' or board[j][3] == 'O')) or
				((board[0][j] == 'T' or board[0][j] == 'O') and (board[1][j] == 'T' or board[1][j] == 'O') and (board[2][j] == 'T' or board[2][j] == 'O') and (board[3][j] == 'T' or board[3][j] == 'O'))) :
				isSolution = 1;
				break
			if (((board[j][0] == 'T' or board[j][0] == 'X') and (board[j][1] == 'T' or board[j][1] == 'X') and (board[j][2] == 'T' or board[j][2] == 'X') and (board[j][3] == 'T' or board[j][3] == 'X')) or
				((board[0][j] == 'T' or board[0][j] == 'X') and (board[1][j] == 'T' or board[1][j] == 'X') and (board[2][j] == 'T' or board[2][j] == 'X') and (board[3][j] == 'T' or board[3][j] == 'X'))) :
				isSolution = 2;
				break	
			if (((board[0][0] == 'T' or board[0][0] == 'O') and (board[1][1] == 'T' or board[1][1] == 'O') and (board[2][2] == 'T' or board[2][2] == 'O') and (board[3][3] == 'T' or board[3][3] == 'O')) or
				((board[3][0] == 'T' or board[3][0] == 'O') and (board[2][1] == 'T' or board[2][1] == 'O') and (board[1][2] == 'T' or board[1][2] == 'O') and (board[0][3] == 'T' or board[0][3] == 'O'))) :
				isSolution = 1;
				break
			if (((board[0][0] == 'T' or board[0][0] == 'X') and (board[1][1] == 'T' or board[1][1] == 'X') and (board[2][2] == 'T' or board[2][2] == 'X') and (board[3][3] == 'T' or board[3][3] == 'X')) or
				((board[3][0] == 'T' or board[3][0] == 'X') and (board[2][1] == 'T' or board[2][1] == 'X') and (board[1][2] == 'T' or board[1][2] == 'X') and (board[0][3] == 'T' or board[0][3] == 'X'))) :
				isSolution = 2;	
				break		
			if isSolution != 3 :
				for k in range (4):
					if board[k][j] == '.' :
						isSolution = 3
						break

		outFile.write('Case #{0}: '.format(i + 1))
		if isSolution == 1 :
			ans = 'O won\n'
		if isSolution == 2 :
			ans = 'X won\n'
		if isSolution == 3 :
			ans = 'Game has not completed\n'
		if isSolution == 0 :
			ans = 'Draw\n'
		outFile.write(ans)
		inFile.readline()
