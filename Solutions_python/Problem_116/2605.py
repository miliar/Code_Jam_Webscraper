a = [['' for i in range (1, 6)] for j in range (1, 6)]
def check_win(a):
    for i in range(1, 5):
        cw = True
        rw = True
        cr = a[i][1]
        cc = a[1][i]
        if cr == 'T':
            cr = a[i][2]
        if cc == 'T':
            cc = a[2][i]
        if cr == '.':
            rw = False
        else:
            for j in range(2, 5):
                if a[i][j] != cr and a[i][j] != 'T':
                    rw = False
                    break
        if rw or cc == '.':
            cw = False
        else:
            for j in range(2, 5):
                if a[j][i] != cc and a[j][i] != 'T':
                    cw = False
                    break
        if cw:
            return cc
        elif rw:
            return cr
    cd1 = a[1][1]
    d1w = True
    if cd1 == 'T':
        cd1 = a[2][2]
    if a[1][1] != '.':
        for i in range(2, 5):
            if a[i][i] != cd1 and a[i][i] != 'T':
                d1w = False
                break
    cd2 = a[1][4]
    d2w = True
    if cd2 == 'T':
        cd2 = a[2][3]
    if a[1][4] != '.':
        for i in range(2, 5):
            if a[i][5-i] != cd2 and a[i][5-i] != 'T':
                d2w = False
                break
    if d1w:
        return cd1
    elif d2w:
        return cd2
    return 'Draw'

file = open('A-small-attempt0.in')
outwrite = open('R1.txt', mode = 'w')
n = int(file.readline())
for m in range(1, n+1):
    gap = False
    for i in range (1, 5):
        line = file.readline()
        if '.' in line and gap == False:
            gap = True
        for j in range(1, 5):
            a[i][j] = line[(j-1):j]
    file.readline()
    outwrite.write('Case #' + str(m)+ ': ')
    result = check_win(a)
    if result == 'X' or result == 'O':
        outwrite.write(str(result) + ' won' + '\n')
    elif gap == False:
        outwrite.write('Draw' + '\n')
    else:
        outwrite.write('Game has not completed' + '\n')
file.close()
outwrite.close()
        
