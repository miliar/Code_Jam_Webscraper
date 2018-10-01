




def buildBoard(row1,row2,row3,row4):
	board = []
	board.append(row1[:4])
	board.append(row2[:4])
	board.append(row3[:4])
	board.append(row4[:4])
	return board



def solveBoard(board):

	output_string = ""
		
	T_location = []
	for i in range(4):
		for j in range(4):
			if board[i][j] == "T":
				T_location = [i,j]
				board[i][j] = "X"
				break
				
	for i in range(4):
		if (board[i][0]=="X" and board[i][1]=="X" and board[i][2]=="X" and board[i][3]=="X") or(board[0][i]=="X" and board[1][i]=="X" and board[2][i]=="X" and board[3][i]=="X" ):	
			return "X won"
	if (board[0][0]=="X" and board[1][1]=="X" and board[2][2]=="X" and board[3][3]=="X") or (board[0][3]=="X" and board[1][2]=="X" and board[2][1]=="X" and board[3][0]=="X"):
			return "X won"
			
	if T_location:
		board[T_location[0]][T_location[1]] = "O"
	for i in range(4):
		if (board[i][0]=="O" and board[i][1]=="O" and board[i][2]=="O" and board[i][3]=="O") or(board[0][i]=="O" and board[1][i]=="O" and board[2][i]=="O" and board[3][i]=="O" ):	
			return "O won"
	if (board[0][0]=="O" and board[1][1]=="O" and board[2][2]=="O" and board[3][3]=="O") or (board[0][3]=="O" and board[1][2]=="O" and board[2][1]=="O" and board[3][0]=="O"):
			return "O won"
	
	for i in range(4):
		for j in range(4):
			if board[i][j] == ".":
				return "Game has not completed"
	
	
	return "Draw"








infile = open("input.txt","r")
outfile = open("output.txt","w")
first_line_read = False

num_puzzles = int(infile.readline())
for i in range(num_puzzles):
	row1=list(infile.readline())
	row2=list(infile.readline())
	row3=list(infile.readline())
	row4=list(infile.readline())
	blank=infile.readline()
	board = buildBoard(row1,row2,row3,row4)
	outstring = solveBoard(board)
	outfile.write ("Case #" + str(i+1) +": " + outstring + "\n")
		