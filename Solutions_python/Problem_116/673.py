def check(a,p):
    flag = 0
    for i in xrange(4):
        count = 0
        for j in xrange(4):
            if a[i][j] == p or a[i][j] == 'T':
                count += 1
        if count == 4 :
            return True
    
    for j in xrange(4):
        count = 0
        for i in xrange(4):
            if a[i][j] == p or a[i][j] == 'T':
                count += 1
        if count == 4 :
            return True
    count1 = 0
    count2 = 0
    for i in xrange(4):
        if a[i][i] == p or a[i][i] == 'T':
            count1 += 1
        if a[i][3-i] == p or a[i][3-i] == 'T':
            count2 += 1
    if count1 == 4 or count2 == 4:
        return True
    return False


t = int(raw_input())
for ab in xrange(t):
    a = []
    for i in xrange(4):
        a.append(raw_input())
    print "Case #%d:" %(ab+1),
    if check(a,'O'):
        print "O won"
    elif check(a,'X'):
        print "X won"
    elif a[0].count('.') + a[1].count('.') + a[2].count('.') + a[3].count('.') > 0:
        print "Game has not completed"
    else :
        print "Draw"
    raw_input()


