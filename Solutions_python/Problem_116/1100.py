import sys

def hasWon(lines, player):
    # print(lines)
    # columns
    for i in range(4):
        fullLine = True
        for j in range(4):
            if lines[i][j] != player and lines[i][j] != 'T':
                fullLine = False
                break
        if fullLine: return True
    # rows
    for j in range(4):
        fullLine = True
        for i in range(4):
            if lines[i][j] != player and lines[i][j] != 'T':
                fullLine = False
                break
        if fullLine: return True
    # diagonals
    fullLine = True
    for i in range(4):
        if lines[i][i] != player and lines[i][i] != 'T':
            fullLine = False
            break
    if fullLine: return True
    fullLine = True
    for i in range(4):
        # print("lines[%d][%d] = %s" % (i, -1-i, lines[i][-1-i]))
        if lines[i][-1-i] != player and lines[i][-1-i] != 'T':
            fullLine = False
            break
    if fullLine: return True

    return False

def gameFinished(lines):
    for l in lines:
        for c in l:
            if c == '.': return False
    return True

def solve(lines):
    if hasWon(lines, 'X'): return "X won"
    if hasWon(lines, 'O'): return "O won"
    if not gameFinished(lines): return "Game has not completed"
    else: return "Draw"

numcases = int(sys.stdin.readline())
for c in range(numcases):
    # read input
    lines = []
    for i in range(4):
        l = []
        line = sys.stdin.readline()
        for ch in line[:4]:
            l.append(ch)
        lines.append(l)
    print("Case #%d: %s" % (c+1, solve(lines)))
    line = sys.stdin.readline()
