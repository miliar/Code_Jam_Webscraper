def runTest(testnum,board):
    xwon = False
    owon = False
    draw = True
    for i in range(4):
        xrow = True
        orow = True
        for j in range(4):
            if board[i][j]=='X':
                orow = False
            if board[i][j]=='O':
                xrow = False
            if board[i][j]=='.':
                draw = False
                xrow = False
                orow = False
        if xrow:
            out.write("Case #"+str(testnum)+": X won\n")
            return True
        if orow:
            out.write("Case #"+str(testnum)+": O won\n")
            return True
    for i in range(4):
        xcol = True
        ocol = True
        for j in range(4):
            if board[j][i]=='X':
                ocol = False
            if board[j][i]=='O':
                xcol = False
            if board[j][i]=='.':
                draw = False
                xcol = False
                ocol = False
        if xcol:
            out.write("Case #"+str(testnum)+": X won\n")
            return True
        if ocol:
            out.write("Case #"+str(testnum)+": O won\n")
            return True

    xdiag = True
    odiag = True
    for i in range(4):
        if board[i][i]=='X':
            odiag = False
        if board[i][i]=='O':
            xdiag = False
        if board[i][i]=='.':
            draw = False
            xdiag = False
            odiag = False

    if xdiag:
        out.write("Case #"+str(testnum)+": X won\n")
        return True
    if odiag:
        out.write("Case #"+str(testnum)+": O won\n")
        return True

    xdiag = True
    odiag = True
    for i in range(4):
        if board[3-i][i]=='X':
            odiag = False
        if board[3-i][i]=='O':
            xdiag = False
        if board[3-i][i]=='.':
            draw = False
            xdiag = False
            odiag = False

    if xdiag:
        out.write("Case #"+str(testnum)+": X won\n")
        return True
    if odiag:
        out.write("Case #"+str(testnum)+": O won\n")
        return True

    if draw:
        out.write("Case #"+str(testnum)+": Draw\n")
        return True
    else:
        out.write("Case #"+str(testnum)+": Game has not completed\n")
        return True

tests = int(raw_input())
i = 0
out = open('output.txt','w')
while i<tests:
    i+=1
    board = []
    for j in range(4):
        board.append(raw_input().strip())
    #print board
    raw_input()
    runTest(i,board)