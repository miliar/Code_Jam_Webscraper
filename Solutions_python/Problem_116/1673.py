import sys

N = int(sys.stdin.readline())

def checkwin(s, x):
    if s in ['TOOO', 'OTOO', 'OOTO', 'OOOT', 'OOOO']:
        print 'Case #%d: O won' % x
        return True
    elif s in ['TXXX', 'XTXX', 'XXTX', 'XXXT', 'XXXX']:
        print 'Case #%d: X won' % x
        return True
    return False

def handlecase(case):
    board = []
    sawdot = False
    for row in range(4):
        l = sys.stdin.readline().strip()
        if not sawdot:
            sawdot = '.' in l
        board.append(l)
    sys.stdin.readline()
    for r in range(4):
        row = board[r]
        if checkwin(row, case):
            return
    for c in range(4):
        col = ''.join([board[row][c] for row in range(4)])
        if checkwin(col, case):
            return
    diag1 = ''.join([board[i][i] for i in range(4)])
    diag2 = ''.join([board[3][0], board[2][1], board[1][2], board[0][3]])
    if checkwin(diag1, case) or checkwin(diag2, case):
        return
    elif sawdot:
        print 'Case #%d: Game has not completed' % case
    else:
        print 'Case #%d: Draw' % case

for x in range(N):
    handlecase(x+1)
