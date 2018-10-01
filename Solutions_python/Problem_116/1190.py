#!/usr/bin/python

def checkWinner(board, player):
    for row in range(4):
        win = True
        for col in range(4):
            if not (board[row][col] == player or board[row][col] == 'T'):
                win = False
        if win:
            return True
    
    for col in range(4):
        win = True
        for row in range(4):
            if not (board[row][col] == player or board[row][col] == 'T'):
                win = False
        if win:
            return True
    
    win = True
    col = 0
    for row in range(4):
        if not (board[row][col] == player or board[row][col] == 'T'):
            win = False
        col += 1
    if win:
        return True
    
    win = True
    col = 3
    for row in range(4):
        if not (board[row][col] == player or board[row][col] == 'T'):
            win = False
        col -= 1
    return win

def blankFound(board):
    for row in range(4):
        for col in range(4):
            if board[row][col] == '.':
                return True
    return False

##################################################3333

T = int(raw_input())

for case in range(T):
    if case != 0:
        raw_input() # read blank line
    
    board = [[], [], [], []]
    for row in range(4):
        board[row] = raw_input()
    
    if checkWinner(board, 'X'):
        print 'Case #' + str(case+1) + ': X won'
    elif checkWinner(board, 'O'):
        print 'Case #' + str(case+1) + ': O won'
    elif blankFound(board):
        print 'Case #' + str(case+1) + ': Game has not completed'
    else:
        print 'Case #' + str(case+1) + ': Draw'

