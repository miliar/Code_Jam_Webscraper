def didWin(board, player):
    # rows
    rowWin = [True, True, True, True]
    rowResult = False
    for i in xrange(4):
    	for j in xrange(4):
            rowWin[i] = rowWin[i] and (board[i][j]==player or board[i][j]=='T')
        rowResult = rowResult or rowWin[i]

    # columns
    colWin = [True, True, True, True]
    colResult = False
    for i in xrange(4):
    	for j in xrange(4):
            colWin[j] = colWin[j] and (board[i][j]==player or board[i][j]=='T')
    for j in xrange(4):
        colResult = colResult or colWin[j]

    # diagonals
    diagWin = [True, True]
    for i in xrange(4):
        diagWin[0] = diagWin[0] and (board[i][i]==player or board[i][i]=='T')
        diagWin[1] = diagWin[1] and (board[i][3-i]==player or board[i][3-i]=='T')
    diagResult = diagWin[0] or diagWin[1]

    # verdict
    return rowResult or colResult or diagResult

def judge(board):
    if didWin(board, 'X'):
        return 'X won'
    elif didWin(board, 'O'):
        return 'O won'
    else:
        hasDot = False
        for i in xrange(4):
            hasDot = hasDot or ('.' in board[i])
        if hasDot:
            return 'Game has not completed'
        else:
            return 'Draw'

def run(inFile, outFile):
    f = open(inFile, 'r')
    g = open(outFile, 'w')
    first = True
    i = 0
    for line in f:
        if first:
            numBoards = int(line)
            boards = [[] for n in xrange(numBoards)]
            first = False
        elif line == '\n':
            i += 1
        else:
            boards[i].append(line)
    f.close()
    for i in xrange(numBoards):
        g.write('Case #'+str(i+1)+': '+judge(boards[i])+'\n')
    g.close()
