import cStringIO
from sys import stdin

def checkrow(row):
    p = {'X': 0,
         'O': 0,
         '.': 0,
         'T': 0}
    for el in row:
        p[el] += 1
    if p['X'] + p['T'] == 4:
        res = 'X'
    elif p['O'] + p['T'] == 4:
        res = 'O'
    elif p['.'] > 0:
        res = '.'
    else:
        res = None
    return res

T = int(raw_input())
all = cStringIO.StringIO(stdin.read())
t = 0
while T > 0:
    T -= 1
    t += 1
    board = []
    emptyCells = False
    completed = False
    for i in range(4):
        row = all.next()
        board.append(row.strip())
    for i in range(4):
        res = checkrow(board[i])
        if res == 'X' or res == 'O':
            break
        elif res == '.':
            emptyCells = True
        res = checkrow(map(lambda r: r[i], board))
        if res == 'X' or res == 'O':
            break
        elif res == '.':
            emptyCells = True
    if res != 'X' and res != 'O':
        row = map(lambda r: r[1][r[0]], enumerate(board))
        res = checkrow(row)
        if res == '.':
            emptyCells = True

    if res != 'X' and res != 'O':
        row = map(lambda r: r[1][3-r[0]], enumerate(board))
        res = checkrow(row)
        if res == '.':
            emptyCells = True

    if res == 'X':
        res = "X won"
    elif res == 'O':
        res = "O won"
    elif emptyCells == True:
        res = "Game has not completed"
    else:
        res = "Draw"

    print 'Case #'+ str(t) +': ' + res

    try:
        all.next()
    except:
        pass
