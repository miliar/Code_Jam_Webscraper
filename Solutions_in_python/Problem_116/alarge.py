t = input()
for i in xrange(t):
    lns = []

    for j in xrange(4):
        lns += [raw_input()]
    try:
        _ = raw_input()
    except:
        pass
    print 'Case #%d:'%(i+1),
    vxs = [0]*4
    hxs = [0]*4

    vos = [0]*4
    hos = [0]*4
    
    rdx = 0
    rdo = 0
    ldx = 0
    ldo = 0
    
    xwon = 0
    owon = 0
    dots = 0
    for j in xrange(4):
        for k in xrange(4):
            if lns[j][k] == '.':
                dots += 1
                continue
            if lns[j][k] == 'X' or lns[j][k] == 'T':
                hxs[j] += 1
                vxs[k] += 1
                if j == k:
                    rdx += 1
                if j+k == 3:
                    ldx += 1
            if lns[j][k] == 'O' or lns[j][k] == 'T':
                hos[j] += 1
                vos[k] += 1
                if j == k:
                    rdo += 1
                if j+k == 3:
                    ldo += 1
            if k == 3:
                if hxs[j] == 4:
                    #game won by x
                    xwon = 1
                    break
                if hos[j] == 4:
                    #game won by o
                    owon = 1
                    break

    if rdx == 4 or ldx == 4:
        #x won
        xwon = 1
    if rdo == 4 or ldo == 4:
        #o won
        owon = 1
    #columns
    for j in xrange(4):
        if vxs[j] == 4:
            #x won
            xwon = 1
        if vos[j] == 4:
            #o won
            owon = 1
    if owon:
        print 'O won'
        
    if xwon:
        print 'X won'
       
    if not (owon or xwon):
        if dots:
            print 'Game has not completed'
        else:
            print 'Draw'

    
