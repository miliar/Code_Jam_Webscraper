players = ["X", "O"]

def check_board(board):
    v = []
    h = []
    d1 = []
    d2 = []
    for y in range(0, 4):
        v1 = []
        h1 = []
        
        for x in range(0, 4):
            v1.append(board[x][y])
            h1.append(board[y][x])
        
        v.append(v1)
        h.append(h1)
    
    l, m = 0, 0
    n, o = 0, 3
    while l < 4 and m < 4 and n < 4 and o >= 0:
        d1.append(board[l][m])
        d2.append(board[n][o])
        l += 1
        m += 1
        n += 1
        o -= 1

    checks = [d1, d2]
    for c in checks:
        for p in players:
            if c.count(p) == 4 or (c.count(p) == 3 and c.count("T") == 1):
                return "%s won" % (p,)
    p,c = 0,0
    checks2 = [v, h]
    for c1 in checks2:
        for c in c1:
            for p in players:
                if c.count(p) == 4 or (c.count(p) == 3 and c.count("T") == 1):
                    return "%s won" % (p,)

n = int(raw_input())

tc = 1
while tc <= n:
    board = []
    result = "Game has not completed"
    l = 4
    completed = 1
    while l:
        m = list(raw_input().strip())
        if m == []:
            continue
        board.append(m)
        if m.count('.') :
            completed = 0
        l -= 1
    result = check_board(board)
    if result == None: # no one won, let's
                       # check if its a draw or the game has not completed
        if completed:
            result = "Draw"
        else:
            result = "Game has not completed"

    print "Case #%d: %s" % (tc, result)
    tc += 1