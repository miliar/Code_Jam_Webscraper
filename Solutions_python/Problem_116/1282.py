def check(line):
    if not any("." in s for s in line):
        countx = 0
        counto = 0
        for x in line: # poor coding but whatev
            if (x == "X"):
                countx+=1
            elif (x == "O"):
                counto+=1
            if (x == "T"):
                counto+=1
                countx+=1
        if countx == 4: return "X"
        if counto == 4: return "O"

f = open('/Users/michael/Dropbox/Coding/Code Jam/2013/tictactoe/In.in')
numcases = int(f.readline())
for a in range(numcases):
    result = []
    final_result = ""
    gamenotover = False
    print "Case #%d:" % (a+1),

    # 2d array of values
    board = []
    for b in range(4):
        board.append(f.readline().split())
        #check for gamenotover
        if any("." in s for s in board[b]):
            gamenotover = True
        
    for b in board: #Check rows
        result.append( check(b[0]) )

    for b in range(4): #Check columns
        temp = []
        for c in range(4):
            temp.append(board[c][0][b])
        result.append( check(''.join(temp)) )

    temp = []
    for b in range(4): #Check L-R diag
        temp.append(board[b][0][b])
    result.append( check(''.join(temp)) )
    temp = []
    for b in range(4):
        temp.append(board[b][0][3-b])
    result.append( check(''.join(temp)) )

    if ('X' in result):
        final_result = "X won"
    elif ('O' in result):
        final_result = "O won"
    elif (gamenotover):
        final_result = "Game has not completed"
    else:
        final_result = "Draw"
    print final_result
    
    # Advance past newline
    f.readline()

