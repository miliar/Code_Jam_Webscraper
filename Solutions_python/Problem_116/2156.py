
size_of_board = 4

def get_cols(m):
    cols = []
    cols.append([m[0][0], m[1][0], m[2][0], m[3][0]])
    cols.append([m[0][1], m[1][1], m[2][1], m[3][1]])
    cols.append([m[0][2], m[1][2], m[2][2], m[3][2]])
    cols.append([m[0][3], m[1][3], m[2][3], m[3][3]])
    return cols

def get_diagonals(m):
    d = []
    d.append([m[0][0], m[1][1], m[2][2], m[3][3]])
    d.append([m[0][3], m[1][2], m[2][1], m[3][0]])
    return d

def check_winner(m):
    xwin = [['X', 'X', 'X', 'X'],
            ['T', 'X', 'X', 'X'],
            ['X', 'T', 'X', 'X'],
            ['X', 'X', 'T', 'X'],
            ['X', 'X', 'X', 'T']]
#    owin = ['OOOO','TOOO','OTOO','OOTO','OOOT']
    owin = [['O', 'O', 'O', 'O'],
            ['T', 'O', 'O', 'O'],
            ['O', 'T', 'O', 'O'],
            ['O', 'O', 'T', 'O'],
            ['O', 'O', 'O', 'T']]

    flag = True
    for row in m:
        if row in xwin:
            return "X won"
        if row in owin:
            return "O won"
        if '.' in row:
            flag = False

    for col in get_cols(m):
        if col in xwin:
            return "X won"
        if col in owin:
            return "O won"

    for d in get_diagonals(m):
        if d in xwin:
            return "X won"
        if d in owin:
            return "O won"

    if flag:
        return "Draw"
    else:
        return "Game has not completed"
    
inf = open("in.txt")
outf = open("out.txt",'w')

noc = int(inf.readline())

n = 1
case = []
for line in inf:
    if len(line) < 4:
#        print("Case #%d: %s\n" % (n, check_winner(case)))
        outf.write("Case #%d: %s\n" % (n, check_winner(case)))
        case = []
        if n == (noc+1):
            break
        n = n+1
        print (n)
    else:
        case.append([line[0], line[1], line[2], line[3]])

inf.close()
outf.close()
