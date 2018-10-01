def possible():
    global n,board,my,a,b,maxi
    mini=101
    for i in xrange(a):
        for j in xrange(b):
            if board[i][j]<mini:
                mini=board[i][j]
    for i in xrange(a):
        for j in xrange(b):
            if board[i][j]==mini and mini!=101:
                count=0
                for k in xrange(a):
                    if board[k][j]==board[i][j] or board[k][j]==101:
                        count+=1
                if count==a:
                    for k in xrange(a):
                        board[k][j]=101
                    #print board
                    return possible()
                count=0
                for k in xrange(b):
                    if board[i][k]==board[i][j] or board[i][k]==101:
                        count+=1
                if count==b:
                    for k in xrange(b):
                        board[i][k]=101
                    #print board
                    return possible()
    for i in xrange(a):
        for j in xrange(b):
            if board[i][j]!=101:
                return 0
    return 1

global n,board,my,a,b,maxi
infile=open("B-large.in",'r')
outfile=open("output",'w')
lines=infile.readlines()
infile.close()
n=int(lines[0][:-1])
curx=1
#n=input()
for s in xrange(n):
    #a,b=[int(i) for i in raw_input().strip().split()]
    a,b=[int(i) for i in lines[curx][:-1].strip().split()]
    board=[]
    my=[]
    for j in xrange(a):
        board.append([int(i) for i in lines[curx+j+1][:-1].strip().split()])
        #board.append([int(i) for i in raw_input().strip().split()])
        my.append([100]*b)
    curx+=a+1
    if possible():
        outfile.write("Case #"+str(s+1)+": YES\n")
        #print "Case #"+str(s+1)+": YES"
    else:
        outfile.write("Case #"+str(s+1)+": NO\n")
        #print "Case #"+str(s+1)+": NO"
outfile.close()
