
import sys, os

board = []
found_empty = False

def dump_board(board):
    for row in range(4):
        print board[row]

# Tic-Tac-Toe-Tomek is a game played on a 4 x 4 square board. The
# board starts empty, except that a single 'T' symbol may appear in
# one of the 16 squares. There are two players: X and O. They take
# turns to make moves, with X starting. In each move a player puts her
# symbol in one of the empty squares. Player X's symbol is 'X', and
# player O's symbol is 'O'.
# After a player's move, if there is a row, column or a diagonal
# containing 4 of that player's symbols, or containing 3 of her
# symbols and the 'T' symbol, she wins and the game ends. Otherwise
# the game continues with the other player's move. If all of the
# fields are filled with symbols and nobody won, the game ends in a
# draw. See the sample input for examples of various winning
# positions.
# Given a 4 x 4 board description containing 'X', 'O', 'T' and '.'
# characters (where '.' represents an empty square), describing the
# current state of a game, determine the status of the
# Tic-Tac-Toe-Tomek game going on. The statuses to choose from are:
# "X won" (the game is over, and X won)
# "O won" (the game is over, and O won)
# "Draw" (the game is over, and it ended in a draw)
# "Game has not completed" (the game is not over yet)
# If there are empty cells, and the game is not over, you should
# output "Game has not completed", even if the outcome of the game is
# inevitable.

def check_row(board, row, player):
    global found_empty
    for col in range(4):
        if ((board[row][col] == player) or (board[row][col] == 'T')): continue
        else:
            if (board[row][col] == '.'): found_empty = True
            return False
    return True

def check_col(board, col, player):
    global found_empty
    for row in range(4):
        if ((board[row][col] == player) or (board[row][col] == 'T')): continue
        else:
            if (board[row][col] == '.'): found_empty = True
            return False
    return True

def check_diags(board, player):
    global found_empty
    won = True
    for row in range(4):
        col = row
        if ((board[row][col] == player) or (board[row][col] == 'T')): continue
        else:
            if (board[row][col] == '.'): found_empty = True
            won = False
            break
    if (won == True): return True
    won = True
    for row in range(4):
        col = 3 - row
        if ((board[row][col] == player) or (board[row][col] == 'T')): continue
        else:
            if (board[row][col] == '.'): found_empty = True
            return False
    return True;

def check_player(board, player):
    for i in range(4):
        result = check_row(board, i, player)
        if (result == True):
            return True
        result = check_col(board, i, player)
        if (result == True):
            return True
    result = check_diags(board, player)
    return result

def check_board(i, board):
    global found_empty
    X_won = check_player(board, 'X')
    O_won = check_player(board, 'O')
    if ((X_won == True) and (O_won == True)): result = "Draw"
    elif (X_won == True): result = "X won"
    elif (O_won == True): result = "O won"
    else:
        if (found_empty == True): result = "Game has not completed"
        else: result = "Draw"
    print "Case #%d: %s" % (i, result)

def main():
    global found_empty
    infile = open(sys.argv[1])
    test_cnt = int(infile.readline())
    for test in range(test_cnt):
        board = []
        for row in range(4):
            board.append(list(infile.readline()[:-1]))
        infile.readline()
        check_board(test+1, board)
        found_empty = False
    exit(0)

main()

