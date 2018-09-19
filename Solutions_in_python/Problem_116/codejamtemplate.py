def getWinner(board):
    notDone = 'Game has not completed'
    draw = 'Draw'
    for x in xrange(4):
        result = findRowWinner(board[x])
        if result:
            return result
    for columnNum in xrange(4):
        result = findRowWinner(column(board, columnNum))
        if result:
            return result
    result = findRowWinner([board[0][0], board[1][1], board[2][2], board[3][3]])
    if result:
        return result
    result = findRowWinner([board[3][0], board[2][1], board[1][2], board[0][3]])
    if result:
        return result
    for matice in xrange(4):
        if '.' in board[matice]:
            return notDone
    return draw


def column(matrix, i):
    return [row[i] for row in matrix]


def findRowWinner(row):
    xWinner = 'X won'
    yWinner = 'O won'
    x = row.count('X')
    o = row.count('O')
    dot = row.count('.')
    t = row.count('T')
    if(dot > 0):
        return None
    elif (x + t == 4):
        return xWinner
    elif(o + t == 4):
        return yWinner


with open('input.txt', 'r') as f:
    numlines = int(f.readline())
    for x in xrange(0, numlines):
        print 'Case #{0}: {1}'.format(int(x+1), getWinner([list(f.readline().rstrip()), list(f.readline().rstrip()), list(f.readline().rstrip()), list(f.readline().rstrip())]))
        f.readline()
