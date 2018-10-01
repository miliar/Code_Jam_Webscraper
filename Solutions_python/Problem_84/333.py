import sys,copy
input = sys.stdin
def readline():
    return input.readline().strip(' \r\n\t')
ncases = int(readline())

def booleanize(t):
    r = []
    n = 0
    for e in t:
        if e == '#':
            n += 1
            r.append(True)
        else:
            r.append(False)
    return (n, r)

def do_test(input):
    line = readline().split()
    R = int(line[0])
    C = int(line[1])
    tile = []
    ttile = []
    nblue = 0
    for i in range(R):
        ttt = readline()
        tmp = booleanize(ttt)
        nblue += tmp[0]
        tile.append(tmp[1])
        ttile.append(list(ttt))
    if nblue % 4 == 0:
        if nblue == 0:
            ttile
        t = copy.deepcopy(ttile)
        for i in range(R-1):
            for j in range(C-1):
                if tile[i][j] and tile[i+1][j+1] and tile[i][j+1] and tile[i+1][j]:
                    t[i][j] = '/'
                    t[i+1][j] = '\\'
                    t[i][j+1] = '\\'
                    t[i+1][j+1] = '/'
                    tile[i][j] = False
                    tile[i+1][j] = False
                    tile[i][j+1] = False
                    tile[i+1][j+1] = False
        for i in range(R):
            for j in range(C):
                if tile[i][j]:
                    return "Impossible"
        return t
    else:
        return "Impossible"

def draw(a):
    r = []
    for aa in a:
        for e in aa:
            r.append(e)
        r.append('\n')
    return r

for test in range(ncases):
    answer = do_test(input)
    print "Case #%d:" % (test+1)
    if answer == "Impossible":
        print answer
    else:
        print ''.join(draw(answer)),
    sys.stdout.flush()

