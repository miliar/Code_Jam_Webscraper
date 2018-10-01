import sys

# win = True
def check(s, board):
    e = s*4
    for c in xrange(4):
        r = board[0][c] + board[1][c] + board[2][c] + board[3][c]
        r = r.replace('T',s)
        if r == e: return True
        
        r = board[c]
        r = r.replace('T',s)
        if r == e: return True

    l_diag = board[0][0] + board[1][1] + board[2][2] + board[3][3]
    l_diag = l_diag.replace('T',s)
    if l_diag == e: return True

    r_diag = board[0][3] + board[1][2] + board[2][1] + board[3][0]
    r_diag = r_diag.replace('T',s)
    if r_diag == e: return True
   
    return False 
    
f = open(sys.argv[1])
cases  = int(f.readline().strip())

for i in xrange(1,cases+1):
    if i != 1: f.readline() 
    board = []
    answer = "Draw"
    for j in xrange(4):  
        board.append( f.readline().strip() ) 

    x_win = check('X', board)
    if x_win:
        answer = 'X won'
        print "Case #%d: %s"%(i, answer)
        continue

    o_win = check('O', board)
    if o_win:
        answer = 'O won'
        print "Case #%d: %s"%(i, answer)
        continue

    for r in board:
        if '.' in r: 
            answer = 'Game has not completed'
            print "Case #%d: %s"%(i, answer)
            break

    if answer == 'Game has not completed':
        continue

    print "Case #%d: %s"%(i, answer)
