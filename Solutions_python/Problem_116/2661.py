def createResult(case, cond):
    result = "Case #" + str(case) + ": "
    if cond == 'N':
        result += "Game has not completed"
    elif cond == 'X' or cond == 'O':
        result += cond + " won"
    else:
        result += "Draw"
    return result

def checkSet(s):
    if '.' not in s:
        l = len(s)
        if l == 1:
            return s.pop()
        elif l == 2:
            if 'T' in s:
                s.remove('T')
                return s.pop()
    return '.'

def checkRows(board):
    for r in board:
        row = set(r)
        cond = checkSet(row)
        if cond != '.':
            return cond
    return '.'

def checkCols(board):
    for col in range(4):
        column = set([board[0][col],
                      board[1][col],
                      board[2][col],
                      board[3][col]])
        cond = checkSet(column)
        if cond != '.':
            return cond
    return '.'

def checkDiags(board):
    d = set([board[0][0],
         board[1][1],
         board[2][2],
         board[3][3]])
    cond = checkSet(d)
    if cond != '.':
        return cond
    d = set([board[0][3],
         board[1][2],
         board[2][1],
         board[3][0]])
    cond = checkSet(d)
    if cond != '.':
        return cond        
    return '.'

def evaluate(board):
    cond = checkRows(board)
    if(cond != '.'):
        return cond
    cond = checkCols(board)
    if(cond != '.'):
        return cond
    cond = checkDiags(board)
    if(cond != '.'):
        return cond
    for row in board:
        if(row.count('.') > 0):
            return 'N'
    
    
def run():
    out = open('A-large.out','w')
    with open('A-large.in', 'r') as f:
        numCases = int(f.readline()) + 1
        for case in range(1, numCases):
            board = [list(f.readline().strip()),
                     list(f.readline().strip()),
                     list(f.readline().strip()),
                     list(f.readline().strip())]
            f.readline()
            cond = evaluate(board)
            out.write(createResult(case, cond) + "\n")       
run()
