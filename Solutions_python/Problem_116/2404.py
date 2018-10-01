import re
with open("Tic-Tac-Toe-Tomek.in") as f:
    data = f.read()
    cases = int(data[:4])
data = re.split('\n\s*\n', data[4:].strip())

def judge(c, x, y):
    check = 0
    for col in range(4):
        if(board[x][col] == 'T' or board[x][col] == c):
            check += 1
    if check == 4:
        return True
    
    check = 0
    for row in range(4):
        if(board[row][y] == 'T' or board[row][y] == c):
            check += 1
    if check == 4:
        return True
    
    check = 0
    
    if(x+y == 3):
        for i in range(4):
            for j in range(4):
                if(i+j == 3):
                    if(board[i][j] == 'T' or board[i][j] == c): 
                        check+=1
        if check == 4:
            return True;
        check = 0;
    
    if(x == y):
        for i in range(4):
            for j in range(4):
                if not(i-j):
                    if(board[i][j] == 'T' or board[i][j] == c): 
                        check += 1
        if check == 4:
            return True
        check = 0;
    return False;
    
for g in range(cases):
    
    dl = data[g].split("\n")
    board = []
    for i in xrange(4):
        board.append([])
        for j in xrange(4):
            board[i].append(dl[i][j])
    
    full = True
    
    winner = "Draw";
    for i in range(4):
        for j in range(4):
            
            if(board[i][j] == '.'): full = False
            
            else: 
                if(board[i][j] == 'X' or board[i][j] == 'O'):
                    if(judge(board[i][j], i, j)):
                        winner = board[i][j]
                        break;
    
    
    print "Case #%s:" % (g + 1),
    if(winner == "X" or winner == "O"): 
        print "%s won\n" % winner,
    else: 
        if(winner == "Draw"):
            if(full): print "Draw"
            else: print "Game has not completed"

       


