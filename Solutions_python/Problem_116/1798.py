import sys

L = ""
T = 1
N = 1

def getCaseData(fp):
    global L
    board = [[0 for x in xrange(4)] for x in xrange(4)]

    for i in range(0,4):
        L = fp.readline()
        for j in range (0,4):
            board[i][j] = L[j]

    fp.readline()
    return board


def checkGame(board):
    global N, L, T
    i = 0
    line = [[0 for x in xrange(4)] for x in xrange(4)]
    line2 = [[0 for x in xrange(4)] for x in xrange(4)]
    line3 = [[0 for x in xrange(4)] for x in xrange(4)]

    winner = ('.', False)
    while(not winner[1] and i < 4):
        line = board[i]
        empty = checkEmptyLine(line)
        winner = checkWinner(line)
        i += 1

    if not winner[1]:
        i = 0
        while(not winner[1] and i < 4):
            for j in range(0,4):
                line2[j] = board[j][i]
            empty = checkEmptyLine(line2)
            winner = checkWinner(line2)
            i += 1

    if not winner[1]:
        #First diagonal
        for i in range(0,4):
            line3[i] = board[i][i]
        empty = checkEmptyLine(line3)
        if not empty:
            winner = checkWinner(line3)
    if not winner[1]:
        #Second diagonal
        for i in range(0,4):
            line3[i] = board[i][len(board[i])-i-1]
        empty = checkEmptyLine(line3)
        if not empty:
            winner = checkWinner(line3)

    if winner[1]:
        return "{0} won".format(winner[0])
    if isBoardFull(board):
        return "Draw"
    else:
        return "Game has not completed"
    #print "Case #{0}: {1}".format(int(N), tstr)

def isBoardFull(board):
    for i in range(0,4):
        for j in range(0,4):
            if board[i][j] == '.':
                return False
    return True

def checkEmptyLine(line):
    for i in range(0,4):
        if line[i] == '.':
            return True
    return False

def checkWinner(line):
    firsttoken = ""
    token = ""
    firsttoken = line[0]
    if firsttoken == '.':
        return ('.', False)

    for i in range(0,4):
        if firsttoken == 'T':
            firsttoken = line[i]
        elif firsttoken == '.':
            return ('.', False)

        token = line[i]

        if firsttoken != token and token != 'T':
            return (firsttoken, False)
    return (firsttoken, True)

def main(argv):
    global N, L,T
    infile = argv[0]
    #open file
    fp = open(infile)

    T = fp.readline()

    for i in range(0, int(T)):
        board = getCaseData(fp)
        status = checkGame(board)
        print "Case #{0}: {1}".format(N, status)
        N += 1

if __name__ == "__main__":
    main(sys.argv[1:])
