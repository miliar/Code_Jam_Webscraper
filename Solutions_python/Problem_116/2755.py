import sys
import itertools

def readBoard():
    board = []
    for i in range(0,4):
        row = []
        for char in sys.stdin.readline().strip():
            row.append(char)
        board.append(row)
    return board

def checkEqual(iterator):
  try:
     iterator = iter(iterator)
     first = next(iterator)
     if (first == 'T'):
         first = next(iterator)
     return (first != '.' and all(first == rest or rest =='T' for rest in iterator), first)
  except StopIteration:
     return (False, first)

def checkBoardState(board):
    #checkhorizontal
    for i in range(0,4):
        eq, first = checkEqual(board[i])
        if eq:
            return "%s won" % first
    #check vertical
    for i in range(0,4):
        check = []
        for j in range(0,4):
            check.append(board[j][i])
        eq, first = checkEqual(check)
        if eq:
            return "%s won" % first
    #check diagonal
    check = [board[0][0], board[1][1], board[2][2], board[3][3]]
    eq = checkEqual(check)
    eq, first = checkEqual(check)
    if eq:
        return "%s won" % first
    check = [board[0][3], board[1][2], board[2][1], board[3][0]]
    eq = checkEqual(check)
    eq, first = checkEqual(check)
    if eq:
        return "%s won" % first
   #check draw
    for i in range(0,4):
        for i in range(0,4):
            if (board[i][j] == '.'):
                return "Game has not completed"
    return "Draw"

numCases = int(raw_input())
for i in range(0,numCases):
    board = readBoard()
    sys.stdin.readline()
    print "Case #%d: %s" % (i+1, checkBoardState(board))
