'''
Created on Apr 12, 2013
@author: jean
'''

XWON="X won"
OWON="O won"

def game(board):
    #print board
    for i in xrange(4):
        X=0
        Y=0
        for j in xrange(4):
            if board[i][j] == "X": X += 1
            if board[i][j] == "O": Y += 1
            if board[i][j] == "T": 
                X += 1
                Y += 1
        if X>3: return XWON
        if Y>3: return OWON
        
    for i in xrange(4):
        X=0
        Y=0
        for j in xrange(4):
            if board[j][i] == "X": X += 1
            if board[j][i] == "O": Y += 1
            if board[j][i] == "T": 
                X += 1
                Y += 1
        if X>3: return XWON
        if Y>3: return OWON

    X=0
    Y=0
    for i in xrange(4):
        if board[i][i] == "X": X += 1
        elif board[i][i] == "O": Y += 1
        elif board[i][i] == "T": 
            X += 1
            Y += 1
    if X>3: return XWON
    if Y>3: return OWON

    X=0
    Y=0
    for i in xrange(4):
        if board[i][3-i] == "X": X += 1
        elif board[i][3-i] == "O": Y += 1
        elif board[i][3-i] == "T": 
                X += 1
                Y += 1
    if X>3: return XWON
    if Y>3: return OWON

    for i in xrange(4):
        for j in xrange(4):
            if board[i][j] == ".":
                return "Game has not completed"
            
    return "Draw"

def main(inp,outp):
    N = int(inp.readline())
    for i in xrange(N):
        l=[]
        for j in xrange(4):
            l.append(inp.readline().strip())
        inp.readline()
        res = game(l)
        outp.write ("Case #%d: %s\n" % (i + 1, res))

def alt():
    N = int(raw_input())
    for i in xrange(N):
        l=[]
        for j in xrange(4):
            line = raw_input()
            l.append(line)
        if i+1<N: line = raw_input()
        print ('Case #%d: ' % (i + 1)) + game(l)

            
if __name__ == '__main__':
    import sys
    #main(sys.stdin,sys.stdout)
    inf=open("A-large.in","rU")
    ouf=open("A-large.out","w")
    main(inf,ouf)
    inf.close()
    ouf.close()            