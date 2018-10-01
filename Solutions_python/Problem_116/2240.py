def chkrow(board, sym):
    
    for i in range(4):
        count = 0
        for j in range(4):
            if board[i][j] == sym or board[i][j] == 'T':
                count += 1
        if count == 4:
            return 1
    return 0

def chkcol(board, sym):

    for i in range(4):
        count = 0
        for j in range(4):
            if board[j][i] == sym or board[j][i] == 'T':
                count += 1
            if count == 4:
                return 1
    return 0

def chkdiaglead(board, sym):
    count = 0
    for i in range(4):
        
        if board[i][i] == sym or board[i][i] == 'T':
            count += 1
        if count == 4:
            return 1
    return 0

def chkdiaglag(board, sym):
    count = 0
    for i in range(4):
        
        if board[i][3-i] == sym or board[i][3-i] == 'T':
            count += 1
        if count == 4:
            return 1
    return 0

def chkempty(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == '.':
                return 1
    return 0

def runprog(FILE):
    infile = open(FILE)
    line1 = infile.readline()
    T = int(line1.strip('\n'))
    for i in range(T):
        xwin = 0
        owin = 0
        draw = 0
        incomp = 0
        board = []
        for n in range(4):
            line = infile.readline()
            line = line.strip('\n')
            linearr = []
            for j in line:
                linearr.append(j)
            board.append(linearr)
    
        if chkrow(board, 'X') or chkcol(board,'X') or chkdiaglead(board,'X') or chkdiaglag(board,'X'):
            xwin = 1
            print 'Case #' + str(i+1) + ': X won'
        elif chkrow(board, 'O') or chkcol(board,'O') or chkdiaglead(board,'O') or chkdiaglag(board,'O'):
            owin = 1
            print 'Case #' + str(i+1) + ': O won'
        elif chkempty(board):
            incomp = 1
            print 'Case #' + str(i+1) + ': Game has not completed'
        else:
            print 'Case #' + str(i+1) + ': Draw'

        infile.readline()
    
            
            
        
