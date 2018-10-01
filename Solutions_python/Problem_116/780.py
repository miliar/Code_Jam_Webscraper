import time

debug = False

def checkreduceboard(board):

    while board:
        if debug:
            print '---'
            for row in board:
                print row
        nextpass = False
        boardmin = min(min(board[i]) for i in range(len(board)))
        for rc in range(len(board)):
            for cc in range(len(board[0])):
                if board[rc][cc] != boardmin:
                    continue
                else:
                    # found one. check horizontal
                    ok = True
                    for i in range(1,len(board[0])):
                        if board[rc][i] != board[rc][i-1]:
                            ok = False
                            break
                    if ok:
                        # remove current row
                        board = board[:rc] + board[rc+1:]
                    else:
                        for i in range(1,len(board)):
                            if board[i][cc] != board[i-1][cc]:
                                # This was the last chance!
                                return False
                        # it was ok, remove the column
                        for crow in range(len(board)):
                            board[crow] = board[crow][:cc] + board[crow][cc+1:]
                    # must have removed a row or a column to get here
                    nextpass = True
                    break
            if nextpass:
                break
    return True

def checkwin(board,player):
    # look for a T
    foundT = False
    for irow in range(len(board)):
        for icol in range(len(board[0])):
            if board[irow][icol] == 'T':
                foundT = True
                trow = irow
                tcol = icol
                board[trow][tcol] = player
                break
        if foundT == True:
            break
        
    for irow in range(len(board)):
        won = True
        for icol in range(len(board[0])):
            if board[irow][icol] != player:
                won = False
                break
        if won:
            return True

    for icol in range(len(board[0])):
        won = True
        for irow in range(len(board)):
            if board[irow][icol] != player:
                won = False
                break
        if won:
            return True

    won = True
    for i in range(len(board)):
        if board[i][i] != player:
            won = False
            break
    if won:
        return True

    won = True
    for i in range(len(board)):
        if board[3-i][i] != player:
            won = False
            break
    if won:
        return True
            
    if foundT:
        board[trow][tcol] = 'T'
        
    return False

tStart = time.time()

fname = "A-large"

fin = open(fname+".in","r")
flines = fin.readlines()
fin.close()

fout = open(fname+".out","w")

numcases = int(flines[0])

for icase in range(1,numcases+1):
   
    board = list()
    boardFull = True
    for irow in range((icase-1)*5+1,(icase-1)*5+4+1):
        row = list()
        for i in range(4):
            cell = flines[irow][i]
            if cell == ".":
                boardFull = False
            row.append(flines[irow][i])
        board.append(row)

    if checkwin(board,"X"):
        result = "X won"
    elif checkwin(board,"O"):
        result = "O won"
    elif boardFull:
        result = "Draw"
    else:
        result = "Game has not completed"        
    
    outstr = "Case #%d: %s" % (icase,result)
    print outstr
    fout.write("%s\n" % (outstr))
    
fout.close()

tEnd = time.time()

print "run time = %s" % (str((tEnd - tStart)))

    

            
