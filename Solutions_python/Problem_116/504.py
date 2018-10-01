games = int(raw_input())
for i in range(games):
    board = [[],[],[],[]]
    for j in range(4):
        line = raw_input()
        for k in range(4):
            board[j].append(line[k])
    winner = "N"
    emptys = 0
    for j in range(4):
        winX = 1
        winO = 1
        for k in range(4): # check x
            if(board[j][k] == '.'):
                emptys = 1
            if not ((board[j][k] == 'X' ) or (board[j][k] == 'T')):
                winX = 0
            if not ((board[j][k] == 'O' ) or (board[j][k] == 'T')):
                winO = 0
        if(winX):
            winner = 'X'
        if(winO):
            winner = 'O'

    for j in range(4):
        winX = 1
        winO = 1
        for k in range(4): # check x
            if not ((board[k][j] == 'X' ) or (board[k][j] == 'T')):
                winX = 0
            if not ((board[k][j] == 'O' ) or (board[k][j] == 'T')):
                winO = 0
        if(winX):
            winner = 'X'
        if(winO):
            winner = 'O'
            
    winX = 1
    winO = 1
    for j in range(4):
        if not ((board[j][j] == 'X') or (board[j][j] == 'T')):
            winX = 0
        if not ((board[j][j] == 'O') or (board[j][j] == 'T')):
            winO = 0
    if(winX):
        winner = 'X'
    if(winO):
        winner = 'O'
    winX = 1
    winO = 1
    for j in range(4):
        if not ((board[j][3-j] == 'X') or (board[j][3-j] == 'T')):
            winX = 0
        if not ((board[j][3-j] == 'O') or (board[j][3-j] == 'T')):
            winO = 0
    if(winX):
        winner = 'X'
    if(winO):
        winner = 'O'
        
    print "Case #" + repr(i + 1) + ":",
    if(winner == 'X'):
        print "X won"
    elif(winner == 'O'):
        print "O won"
    elif(emptys):
        print "Game has not completed"
    else:
        print "Draw"
    
    raw_input()

