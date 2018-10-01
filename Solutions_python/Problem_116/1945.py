def a(filename):
    f = open(filename,'r')
    g = open('alarge.out','w')
    count = int(f.readline()[:-1])
    for i in xrange(count):
        if i>0:
            f.readline()
        case = "Case #"+str(i+1)+": "
        a = []
        gamecomplete = True
        for j in xrange(4):
            a.append(f.readline())

        #Check rows
        rows = checkRows(a)
        if rows == 1:
            g.write(case+"X won\n")
            continue
        elif rows == 2:
            g.write(case+"O won\n")
            continue
        elif rows == -1:
            gamecomplete = False

        #Check columns 
        cols = checkColumns(a)
        if cols == 1:
            g.write(case+"X won\n")
            continue
        elif cols == 2:
            g.write(case+"O won\n")
            continue

        #Check diagonals
        diags = checkDiagonals(a)
        if diags == 1:
            g.write(case+"X won\n")
            continue
        elif diags== 2:
            g.write(case+"O won\n")
            continue

        if gamecomplete:
            g.write(case+"Draw\n")
        else:
            g.write(case+"Game has not completed\n")

def checkRows(strings):
    # -1 for game incomplete, 0 for none, 1 for X, 2 for O
    gamecomplete = True
    for s in strings:
        countx = 0
        counto = 0
        countt = 0
        for c in s:
            if c=='X':
                countx+=1
            if c=='O':
                counto+=1
            if c=='T':
                countt+=1
            if c=='.':
                gamecomplete=False
        if countx+countt>=4:
            return 1
        elif counto+countt>=4:
            return 2
    if not gamecomplete:
        return -1
    return 0

def checkColumns(strings):
    # -1 for game incomplete, 0 for none, 1 for X, 2 for O
    gamecomplete = True
    for i in xrange(4):
        countx = 0
        counto = 0
        countt = 0
        for j in xrange(4):
            c = strings[j][i]
            if c=='X':
                countx+=1
            if c=='O':
                counto+=1
            if c=='T':
                countt+=1
        if countx+countt>=4:
            return 1
        elif counto+countt>=4:
            return 2
    return 0

def checkDiagonals(strings):
    for j in xrange(2):
        countx = 0
        counto = 0
        countt = 0
        for i in xrange(4):
            if j==0:
                c = strings[i][i]
            else:
                c = strings[i][3-i]
            if c == 'X':
                countx+=1
            if c == 'O':
                counto+=1
            if c == 'T':
                countt+=1
        if countx+countt>=4:
            return 1
        elif counto+countt>=4:
            return 2
    return 0

#a('A-small-attempt0.in')
a('A-large.in')
