import sys

def full(board):
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == '.':
                return False
    return True

def translate(board, legend):
    ret = [[0 for i in range(0, 4)] for i in range(0, 4)]
    for i in range(0, 4):
        for j in range(0, 4):
            ret[i][j] = legend[ board[i][j] ]
    return ret

def winner(board):
    if sum(board[0]) == 4 or \
       sum(board[1]) == 4 or \
       sum(board[2]) == 4 or \
       sum(board[3]) == 4 or \
       board[0][0] + board[1][0] + board[2][0] + board[3][0] == 4 or \
       board[0][1] + board[1][1] + board[2][1] + board[3][1] == 4 or \
       board[0][2] + board[1][2] + board[2][2] + board[3][2] == 4 or \
       board[0][3] + board[1][3] + board[2][3] + board[3][3] == 4 or \
       board[0][0] + board[1][1] + board[2][2] + board[3][3] == 4 or \
       board[3][0] + board[2][1] + board[1][2] + board[0][3] == 4:
        return True

f = open(sys.argv[1], 'r')
T = int(f.readline())
for case in range(0, T):
    board = [[0 for i in range(0, 4)] for i in range(0, 4)]
    for i in range(0, 4):
        line = f.readline()
        for j in range(0, 4):
            board[i][j] = line[j]
    f.readline()                    # burn empty line

    status = None
    if winner(translate(board, {'X': 1, 'O': 0, '.': 0, 'T': 1})):
        status = "X won"
    elif winner(translate(board, {'X': 0, 'O': 1, '.': 0, 'T': 1})):
        status = "O won"
    elif full(board):
        status = "Draw"
    else:
        status = "Game has not completed"
        
    print "Case #%d: %s" % (case + 1, status)
