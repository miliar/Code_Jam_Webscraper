def check(board, player):
    for row in range(4):
        board[row] = board[row].replace('T', player)
        if board[row] == player * 4:
            return True
    for i in range(4):
        if board[0][i] == player and board[1][i] == player and \
           board[2][i] == player and board[3][i] == player:
           return True
    if board[0][0] == player and board[1][1] == player and \
       board[2][2] == player and board[3][3] == player:
       return True
    if board[0][3] == player and board[1][2] == player and \
       board[2][1] == player and board[3][0] == player:
       return True
    return False


f = open('A-large.in', 'r')
nr_cases = int(f.readline())

for i in range(nr_cases):
    board = []
    for x in range(4):
        row = f.readline().replace('\n', '')
        board.append(row)
    f.readline() # empty line

    if check(board[:], 'X'):
        print "Case #%i: X won" % (i+1)
    elif check(board[:], 'O'):
        print "Case #%i: O won" % (i+1)
    else:
        hasDot = False
        for x in range(4):
            if board[x].find('.') >= 0:
                hasDot = True
                break
        if hasDot:
            print "Case #%i: Game has not completed" % (i + 1)
        else:
            print "Case #%i: Draw" % (i + 1)
    
