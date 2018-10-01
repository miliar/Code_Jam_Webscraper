global a
a=open("A-large.in","r")
def InputBoard():
    global a
    j=0
    board=[]
    while(j<4):
        line=a.readline()
        board+=[line[:len(line)-1]]
        j+=1    
    return board
def CheckRow(board):
    i=0
    isOver=True
    while(i<4):
        j=0
        countX=0
        countO=0
        while(j<4):
            if(board[i][j]=='X'):
                countX+=1
            elif(board[i][j]=='O'):
                countO+=1
            elif(board[i][j]=='T'):
                countX+=1
                countO+=1
            else:
                isOver=False
            j+=1
        i+=1
        if(countX==4):
            return 'X'
        if(countO==4):
            return 'O'
    if(isOver==True):
        return 'Draw'
    else:
        return 'Not Over'
def CheckColumn(board):
    i=0
    isOver=True
    while(i<4):
        j=0
        countX=0
        countO=0
        while(j<4):            
            if(board[j][i]=='X'):
                countX+=1
            elif(board[j][i]=='O'):
                countO+=1
            elif(board[j][i]=='T'):
                countX+=1
                countO+=1
            else:
                isOver=False
            j+=1
        i+=1
        if(countX==4):
            return 'X'
        if(countO==4):
            return 'O'
    if(isOver==True):
        return 'Draw'
    else:
        return 'Not Over'
def CheckDiagonals(board):
    i=0
    countX=0
    countO=0
    while(i<4):
        if(board[i][i]=='X'):
            countX+=1
        elif(board[i][i]=='O'):
            countO+=1
        elif(board[i][i]=='T'):
            countX+=1
            countO+=1
        i+=1
    if(countX==4):
        return 'X'
    if(countO==4):
        return 'O'

    i=0
    countX=0
    countO=0
    while(i<4):
        if(board[3-i][i]=='X'):
            countX+=1
        elif(board[3-i][i]=='O'):
            countO+=1
        elif(board[3-i][i]=='T'):
            countX+=1
            countO+=1
        i+=1
    if(countX==4):
        return 'X'
    if(countO==4):
        return 'O'
    return 'Draw'

line=a.readline()
T=int(line[:len(line)-1])
i=1
boards=[]
while(i<=T):
    boards+=[InputBoard()]
    a.readline()    
    i+=1
a.close()
i=0
while(i<T):
    row=CheckRow(boards[i])
    column=CheckColumn(boards[i])
    diagonals=CheckDiagonals(boards[i])
    whowon=""
    if(row=='X' or column=='X' or diagonals=='X'):
        whowon=" X won"
    elif(row=='O' or column=='O' or diagonals=='O'):
        whowon=" O won"
    elif(row=='Not Over' or column=='Not Over'):
        whowon=" Game has not completed"
    else:
        whowon=" Draw"
    print("Case #"+str(i+1)+":"+whowon)
    i+=1
        
