##Problem
##
##Tic-Tac-Toe-Tomek is a game played on a 4 x 4 square board. The board starts empty, except that a single 'T' symbol may appear in one of the 16 squares. There are two players: X and O. They take turns to make moves, with X starting. In each move a player puts her symbol in one of the empty squares. Player X's symbol is 'X', and player O's symbol is 'O'.
##
##After a player's move, if there is a row, column or a diagonal containing 4 of that player's symbols, or containing 3 of her symbols and the 'T' symbol, she wins and the game ends. Otherwise the game continues with the other player's move. If all of the fields are filled with symbols and nobody won, the game ends in a draw. See the sample input for examples of various winning positions.
##
##Given a 4 x 4 board description containing 'X', 'O', 'T' and '.' characters (where '.' represents an empty square), describing the current state of a game, determine the status of the Tic-Tac-Toe-Tomek game going on. The statuses to choose from are:
##
##"X won" (the game is over, and X won)
##"O won" (the game is over, and O won)
##"Draw" (the game is over, and it ended in a draw)
##"Game has not completed" (the game is not over yet)
##If there are empty cells, and the game is not over, you should output "Game has not completed", even if the outcome of the game is inevitable.
##Input
##
##The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of 4 lines with 4 characters each, with each character being 'X', 'O', '.' or 'T' (quotes for clarity only). Each test case is followed by an empty line.
##
##Output
##
##For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is one of the statuses given above. Make sure to get the statuses exactly right. When you run your code on the sample input, it should create the sample output exactly, including the "Case #1: ", the capital letter "O" rather than the number "0", and so on.


# Get input file
input_fname = input("Input filename: ")
infile = open(input_fname, 'r')
# Set output file
output_fname = input_fname.replace("in", "out")
outfile = open(output_fname, 'w')

N = int(infile.readline().strip("\n"))

for casenum in range(N):
    print("Case #", casenum+1, ": ", sep="", end="", file=outfile)

    board = []
    for x in range(4):
        board.append(infile.readline().strip("\n"))
    # read the blank line between the data sets
    infile.readline()

    ## Check to see if X has won
    # Check columns
    xwin_col = True
    for col in range(4):
        xwin_col = True
        for row in range(4):
            if board[row][col] not in ['X', 'T']:
                xwin_col = False
        if xwin_col:
            break
        
    # Check rows
    xwin_row = True
    for row in range(4):
        xwin_row = True
        for col in range(4):
            if board[row][col] not in ['X', 'T']:
                xwin_row = False
        if xwin_row:
            break
    # Check diagonals
    xwin_diag1 = True
    xwin_diag2 = True
    for row in range(4):
        if board[row][3-row] not in ['X', 'T']:
            xwin_diag1 = False
        if board[row][row] not in ['X', 'T']:
            xwin_diag2 = False

    xwin = xwin_row or xwin_col or xwin_diag1 or xwin_diag2
    if xwin:
        print("X won", end='', file=outfile)
        
    ## Check to see if O has won
    # Check columns
    owin_col = True
    for col in range(4):
        owin_col = True
        for row in range(4):
            if board[row][col] not in ['O', 'T']:
                owin_col = False
        if owin_col:
            break
        
    # Check rows
    owin_row = True
    for row in range(4):
        owin_row = True
        for col in range(4):
            if board[row][col] not in ['O', 'T']:
                owin_row = False
        if owin_row:
            break
    # Check diagonals
    owin_diag1 = True
    owin_diag2 = True
    for row in range(4):
        if board[row][3-row] not in ['O', 'T']:
            owin_diag1 = False
        if board[row][row] not in ['O', 'T']:
            owin_diag2 = False

    owin = owin_row or owin_col or owin_diag1 or owin_diag2
    if owin:
        print("O won", end='', file=outfile)


    ## Check to see if the game is over
    full_board = True
    for row in range(4):
        if '.' in board[row]:
            full_board = False

    if full_board and not xwin and not owin:
        print("Draw", end='', file=outfile)
    elif not full_board and not xwin and not owin:
        print("Game has not completed", end='', file=outfile)
        
    print("", file=outfile)
# end case loop

infile.close()
outfile.close()
