def countValues(line):
    return {'X' : line.count('X'), 'O': line.count('O'), 'T': line.count('T'), '.': line.count('.')}

def evalHorizontal(line):
    c = countValues(line)
    
    if (c['X'] == 4 or (c['X'] == 3 and c['T'] == 1)):
        return 'X'
    elif (c['O'] == 4 or (c['O'] == 3 and c['T'] == 1)):
        return 'O'
    else:
        return None
    # else:
    #     return c

def getLeftDiagonal(board):
    return [board[0][0], board[1][1], board[2][2], board[3][3]]

def getRightDiagonal(board):
    return [board[0][3], board[1][2], board[2][1], board[3][0]]
    

def evalDiagonal(diag):    
    if ((diag.count('X') == 3 and diag.count('T') == 1) or  diag.count('X') == 4):
        return 'X'
    elif((diag.count('O') == 3 and diag.count('T') == 1) or  diag.count('O') == 4 ):
        return 'O'
    else:
        return None                
                
def evalVerticalOrDraw(board):

    dot = 0    
    for i in range(4):
        x = 0
        o = 0
        t = 0        

        for j in range(4):                            
            if(board[j][i] == 'X'):
                x += 1
            elif(board[j][i] == 'O'):
                o += 1
            elif(board[j][i] == 'T'):
                t = 1
            elif(board[j][i] == '.'):
                dot = 1

        if (x == 4 or (x == 3 and t == 1)):
            return 'X'
        elif (o == 4 or (o == 3 and t == 1)):
            return 'O'

    if(dot == 0):
        return 'Draw'

def readState(f):
    board = []
    result = None
    for i in range(5):
        line = f.readline()
        
        if(not result and line !='\n' and line != ''):
            res = evalHorizontal(line)
            board.append(line)
            if(res): 
                result = res
    if(result):
        return result
    if(board[0][0] != '.'):
        lDiagonal = getLeftDiagonal(board)
        # print('left Diagonal:')
        # print(lDiagonal)
        res = evalDiagonal(lDiagonal)
    if(res):
        return res
    elif (board[0][3] != '.'):
        rDiagonal = getRightDiagonal(board)
        # print('right Diagonal:')
        # print(rDiagonal)
        res = evalDiagonal(rDiagonal)

        if(res):
            return res
        # if(res): 
        #     print('res: '+res)
        # else:
        #     print('Not winning diagonal')
    res = evalVerticalOrDraw(board)
    return evalVerticalOrDraw(board)
    
if __name__ == "__main__":
    
    f = open('input.txt','r')
    numCases = int(f.readline())

    #print('numCaseS: '+str(numCases))
    i = 1
    f2 = open('output.txt','w')
    while(i <= numCases):
        #print('\nCase: '+str(i))
        res = readState(f)

        if(res == 'X' or res == 'O'):
            f2.write('Case #'+str(i)+": "+res+" won\n")
        elif(res == 'Draw'):
            f2.write('Case #'+str(i)+": Draw\n")
        else:
            f2.write('Case #'+str(i)+": Game has not completed\n")
        i += 1
    f2.close()
        #print('---------------------------------')
    

