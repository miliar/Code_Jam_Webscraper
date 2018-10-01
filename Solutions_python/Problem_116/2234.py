#python

def is_val_or_t(board, x, y, val):
    return (board[x][y] == val or board[x][y] == 'T')

def has_empty(board):
    for i in xrange(4):
        for j in xrange(4):
            if board[i][j] == '.':
                return 1
    
def check_win(board, val):
    #check rows
    for i in xrange(4):
        if is_val_or_t(board, i, 0, val) and is_val_or_t(board, i, 1, val) and is_val_or_t(board, i, 2, val) and is_val_or_t(board, i, 3, val):
            return 1
        
        if is_val_or_t(board, 0, i, val) and is_val_or_t(board, 1, i, val) and is_val_or_t(board, 2, i, val) and is_val_or_t(board, 3, i, val):
            return 1
    
    #diagonal
    if is_val_or_t(board, 0, 0, val) and is_val_or_t(board, 1, 1, val) and is_val_or_t(board, 2, 2, val) and is_val_or_t(board, 3, 3, val):
        return 1
    
    if is_val_or_t(board, 0, 3, val) and is_val_or_t(board, 1, 2, val) and is_val_or_t(board, 2, 1, val) and is_val_or_t(board, 3, 0, val):
        return 1
    
    return 0

def parse_case():
    board = []
    for i in xrange(4):
        board.append(raw_input())
    
    try:
        raw_input()
    except:
        return board
    
    return board
#main

num = int(raw_input())

for i in xrange(num):
    board = parse_case()
    case = i+1

    if check_win(board, 'X'):
        print 'Case #%d: X won' % case
    elif check_win(board, 'O'):
        print 'Case #%d: O won' % case
    elif has_empty(board):
        print 'Case #%d: Game has not completed' % case
    else:
        print 'Case #%d: Draw' % case