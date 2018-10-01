import sys

T = int(raw_input())
for i in xrange(1, T + 1):
    board = []
    for j in xrange(4):
        board.append(list(raw_input().strip()))
    empty = 0
    winX = False
    winO = False
    for j in xrange(4):
#        print board[j]
        countX = 0
        countO = 0
        countT = 0
        for k in xrange(4):
            if board[j][k] == '.':
                empty += 1
            elif board[j][k] == 'X':
                countX += 1
            elif board[j][k] == 'O':
                countO += 1
            elif board[j][k] == 'T':
                countT += 1
        if countX == 4 or (countX == 3 and countT == 1):
            winX = True
        elif countO == 4 or (countO == 3 and countT == 1):
            winO = True
    for k in xrange(4):
#        print board[j]
        countX = 0
        countO = 0
        countT = 0
        for j in xrange(4):
            if board[j][k] == '.':
                empty += 1
            elif board[j][k] == 'X':
                countX += 1
            elif board[j][k] == 'O':
                countO += 1
            elif board[j][k] == 'T':
                countT += 1
        if countX == 4 or (countX == 3 and countT == 1):
            winX = True
        elif countO == 4 or (countO == 3 and countT == 1):
            winO = True
    countX = 0
    countO = 0
    countT = 0
    for j in xrange(4):
        if board[j][j] == '.':
            empty += 1
        elif board[j][j] == 'X':
            countX += 1
        elif board[j][j] == 'O':
            countO += 1
        elif board[j][j] == 'T':
            countT += 1
    if countX == 4 or (countX == 3 and countT == 1):
        winX = True
    elif countO == 4 or (countO == 3 and countT == 1):
        winO = True
    countX = 0
    countO = 0
    countT = 0
    for j in xrange(4):
        if board[j][3 - j] == '.':
            empty += 1
        elif board[j][3 - j] == 'X':
            countX += 1
        elif board[j][3 - j] == 'O':
            countO += 1
        elif board[j][3 - j] == 'T':
            countT += 1
    if countX == 4 or (countX == 3 and countT == 1):
        winX = True
    elif countO == 4 or (countO == 3 and countT == 1):
        winO = True
    if winX:
        result = 'X won'
    elif winO:
        result = 'O won'
    elif empty == 0:
        result = 'Draw'
    else:
        result = 'Game has not completed'
    
    print "Case #{0}: {1}".format(i, result)
    raw_input()

