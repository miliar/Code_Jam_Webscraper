f = open("a.in")
T = int(f.readline())
for i in range(T):
    board = []
    for j in range(4):
        board.append(f.readline()[:-1])
    xWin = False
    oWin = False
    emptyspace = False
    
    #Check rows
    
    for row in board:
        startchar = None
        if row[0] != 'T':
            startchar = row[0]
        else:
            startchar = row[1]
        for char in row:
            if char == '.':
                emptyspace = True
            if char!= 'T' and char != startchar:
                break
        else:
            if startchar == 'X':
                xWin = True
            elif startchar == 'O':
                oWin = True

    #Check cols
    for x in range(4):
        startchar = None
        if board[0][x] != 'T':
            startchar = board[0][x]
        else:
            startchar = board[1][x]
        for y in range(4):
            if board[y][x] != 'T' and board[y][x] != startchar:
                break
        else:
            if startchar == 'X':
                xWin = True
            elif startchar == 'O':
                oWin = True
            
            
            
    
    #check diag
    startchar = None
    if board[0][0] != "T":
        startchar = board[0][0]
    else:
        startchar = board[1][1]
    for x in range(4):
        if board[x][x] != 'T' and board[x][x] != startchar:
            break
    else:
        if startchar == 'X':
            xWin = True
        elif startchar == 'O':
            oWin = True

    startchar = None
    if board[3][0] != "T":
        startchar = board[3][0]
    else:
        startchar = board[2][1]
    for x in range(4):
        if board[3-x][0+x] != 'T' and board[3-x][0+x] != startchar:
            break
    else:
        if startchar == 'X':
            xWin = True
        elif startchar == 'O':
            oWin = True        


    if not xWin and not oWin:
        if emptyspace:
            print "Case #%d: Game has not completed" %(i+1)
        else:
            print "Case #%d: Draw" % (i+1)
    elif xWin:
        print "Case #%d: X won" % (i+1)
    else:
        print "Case #%d: O won" % (i+1)
    f.readline()
    
        
