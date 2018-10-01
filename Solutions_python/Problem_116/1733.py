def findState(board):
    XWON = "X won"
    OWON = "O won"
    DRAW = "Draw"
    INCOMP = "Game has not completed"
    for i in range(len(board)):
        xCount = 0
        oCount = 0
        tCount = 0
        if 'X' in board[i]:
            xCount = board[i].count('X')
        if 'O' in board[i]:
            oCount = board[i].count('O')
        if 'T' in board[i]:
            tCount = 1
        if(xCount == 4 or (xCount+tCount) == 4):
            return XWON
        if(oCount == 4 or (oCount+tCount) == 4):
            return OWON

    transposeBoard = []
    for x in zip(*board):
       transposeBoard += [x]
   
    for i in range(len(transposeBoard)):
        xCount = 0
        oCount = 0
        tCount = 0
        if 'X' in transposeBoard[i]:
            xCount = transposeBoard[i].count('X')
        if 'O' in transposeBoard[i]:
            oCount = transposeBoard[i].count('O')
        if 'T' in transposeBoard[i]:
            tCount = 1
        if(xCount == 4 or (xCount+tCount) == 4):
            return XWON
        if(oCount == 4 or (oCount+tCount) == 4):
            return OWON
    xCount = 0
    oCount = 0
    tCount = 0
    for i in range(4):
        if board[i][i] == "X":
            xCount += 1
        if board[i][i] == "O":
            oCount += 1
        if board[i][i] == "T":
            tCount += 1
    if(xCount == 4 or (xCount+tCount) == 4):
            return XWON
    if(oCount == 4 or (oCount+tCount) == 4):
            return OWON

    xCount = 0
    oCount = 0
    tCount = 0
    for i in [3,2,1,0]:
        if board[i][3-i] == "X":
            xCount += 1
        if board[i][3-i] == "O":
            oCount += 1
        if board[i][3-i] == "T":
            tCount += 1
    if(xCount == 4 or (xCount+tCount) == 4):
            return XWON
    if(oCount == 4 or (oCount+tCount) == 4):
            return OWON

    dotCount = 0
    for i in range(len(board)):
        if '.' in board[i]:
            return INCOMP

    return DRAW

f = open('A-large.in', 'r')
N = int(f.readline())
output = []
for i in range(N):    
    board = []
    for p in range(4): #rows
        readLine = f.readline()
        line = []
        for j in range(4): #columns
            line += [readLine[j]]
        board += [line]
    f.readline()
    
    output += ["Case #"+str(i+1)+": " + findState(board)]


f.close()
output = '\n'.join(e for e in output)
f = open('a-large.out', 'w')
f.write(output)
f.close()



        
        
