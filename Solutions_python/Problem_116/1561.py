T = input()

answers = ["X won", "O won", "Draw", "Game has not completed"]

def check(M):
    for i in xrange(4):
        won = True
        for j in xrange(4):
            won = won and (M[i][j] == 'X' or M[i][j] == 'T')
        if won:
            return 0
        won = True
        for j in xrange(4):
            won = won and (M[i][j] == 'O' or M[i][j] == 'T')
        if won:
            return 1
        won = True
        for j in xrange(4):
            won = won and (M[j][j] == 'X' or M[j][j] == 'T')
        if won:
            return 0
        won = True
        for j in xrange(4):
            won = won and (M[j][j] == 'O' or M[j][j] == 'T')
        if won:
            return 1
        for j in xrange(4):
            won = won and (M[j][3-j] == 'X' or M[j][3-j] == 'T')
        if won:
            return 0
        won = True
        for j in xrange(4):
            won = won and (M[j][3-j] == 'O' or M[j][3-j] == 'T')
        if won:
            return 1
    return -1

for i in xrange(T):
    M = []
    for j in xrange(4):
        M.append(raw_input())
    if i+1!= T :raw_input()
    option = check(M)
    if option != -1:
        print "Case #{0}: {1}".format(i+1, answers[option])
        continue
    option = check(zip(*M))
    if option != -1:
        print "Case #{0}: {1}".format(i+1, answers[option])
        continue
    for j in xrange(4):
        for k in xrange(4):
            if M[j][k] == '.':
                option = 3
    
    if option == 3:
        print "Case #{0}: {1}".format(i+1, answers[option])
    else:
        print "Case #{0}: {1}".format(i+1, answers[2])


