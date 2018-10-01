__author__ = 'nilsonjr'


f = open('in2.txt')

n = f.readline()
print n


def result(game):
    #line
    for i in range(4):
        won = True
        line_chr = ''
        for j in range(4):
            if j == 0:
                if game[i][j] == '.':
                    won = False
                    break
                line_chr = game[i][j]
            elif game[i][j] != line_chr and game[i][j] != 'T':
                    won = False
                    break
        if won:
            return line_chr+" won"


    #col
    for j in range(4):
        won = True
        line_chr = ''
        for i in range(4):
            #print i, j, game[i][j]
            if i == 0:
                if game[i][j] == '.':
                    won = False
                    break
                line_chr = game[i][j]
            elif game[i][j] != line_chr and game[i][j] != 'T':
                won = False
                break

        if won:
            return line_chr+" won"


    #diag
    won = True
    line_chr = ''
    for j in range(4):
        if j == 0:
            if game[j][j] == '.':
                won = False
                break
            line_chr = game[j][j]
        elif game[j][j] != line_chr and game[j][j] != 'T':
            won = False
            break
    if won:
        return line_chr+" won"


    #diag2
    won = True
    line_chr = ''
    for j in range(4):
        if j == 0:
            if game[j][3-j] == '.':
                won = False
                break
            line_chr = game[j][3-j]
        elif game[j][3-j] != line_chr and game[j][3-j] != 'T':
            won = False
            break
    if won:
        return line_chr+" won"


    has_dot = False
    for i in range(4):
        for j in range(4):
            if game[i][j] == '.':
                return "Game has not completed"

    return "Draw"


for i in range(int(n)):
    lst = []
    for j in range(4):
        line = f.readline()
        l1 = []
        for s in line:
            if s != '\n':
                l1.append(s)
        lst.append(l1)
    print "Case #"+str(i+1)+": "+result(lst)
    #print lst
    f.readline()
