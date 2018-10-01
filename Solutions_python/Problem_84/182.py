T = input()
for testcase in range(T):
    [R,C] = [int(x) for x in raw_input().split()]
    board = []
    for _ in range(R):
        board.append(raw_input())

    cfs = [False for _ in range(C+1)]
    nfs = [False for _ in range(C+1)]

    f = False
    for j,row in enumerate(board):
        for i,p in enumerate(row):
            if p == '#':
                if cfs[i]:
                    pass
                elif j < R-1 and i < C-1:
                    cfs[i+1] = True
                    nfs[i] = True
                    nfs[i+1] = True
                else:
                    f = True
                    break
            else:
                if cfs[i]:
                    f = True
                    break
                else:
                    pass
        if f:
            break
        cfs = nfs
        nfs = [False for _ in range(C+1)]


    if f:
        print "Case #%i:" % (testcase+1)
        print 'Impossible'
    else:
        print "Case #%i:" % (testcase+1)
        for i in range(R):
            for j in range(C):
                if board[i][j] == '#':
                    board[i] = board[i][:j] + '/\\' + board[i][j+2:]
                    board[i+1] = board[i+1][:j] + '\\/' + board[i+1][j+2:]
        for row in board:
            print row
        


