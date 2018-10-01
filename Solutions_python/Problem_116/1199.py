import sys

inp2 = '3\nXOXT\nXXOO\nOXOX\nXXOO\nXOX.\nOX..\n....\n....\nOOXX\nOXXX\nOX.T\nO..O'

def check_state(num, board):
    for r in board:
        x = 0
        o = 0
        t = False
        for c in r:
            if c == 'X':
                x += 1
            elif c == 'T':
                t = True
            elif c == 'O':
                o += 1
        if x == 4 or (x == 3 and t):
            print "Case #" + str(num) + ": " + "X won"
            return
        elif o == 4 or (o == 3 and t):
            print "Case #" + str(num) + ": " + "O won"
            return

    for c in xrange(4):
        x = 0
        o = 0
        t = False
        for r in xrange(4):
            if board[r][c] == 'X':
                x += 1
            elif board[r][c] == 'T':
                t = True
            elif board[r][c] == 'O':
                o += 1
        if x == 4 or (x == 3 and t):
            print "Case #" + str(num) + ": " + "X won"
            return
        elif o == 4 or (o == 3 and t):
            print "Case #" + str(num) + ": " + "O won"
            return

    x1 = 0
    x2 = 0
    o1 = 0
    o2 = 0
    t1 = False
    t2 = False
    for i in xrange(4):
        if board[i][i] == 'X':
            x1 += 1
        elif board[i][i] == 'T':
            t1 = True
        elif board[i][i] == 'O':
            o1 += 1
        if board[i][3-i] == 'X':
            x2 += 1
        elif board[i][3-i] == 'T':
            t2 = True
        elif board[i][3-i] == 'O':
            o2 += 1

    if x1 == 4 or (x1 == 3 and t1) or x2 == 4 or (x2 == 3 and t2):
        print "Case #" + str(num) + ": " + "X won"
        return
    elif o1 == 4 or (o1 == 3 and t1) or o2 == 4 or (o2 == 3 and t2):
        print "Case #" + str(num) + ": " + "O won"
        return

    for r in board:
        for c in r:
            if c == '.':
                print "Case #" + str(num) + ": " + "Game has not completed"
                return

    print "Case #" + str(num) + ": " + "Draw"


# input = inp2
input = sys.argv[1]
with open(input) as f:
    lines = f.readlines()
size = int(lines[0])
lines = lines[1:]
for i in xrange(size):
    board = lines[0:4]
    lines = lines[5:]
    check_state(i+1, board)

