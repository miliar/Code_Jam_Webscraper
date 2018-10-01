

def readinput(filename):
    f = open(filename, 'r')
    cases = int(f.readline().strip())
    boards = []
    for i in range(cases):
        n,m = [int(x) for x in f.readline().strip().split()]
        yield tuple(tuple(int(x) for x in f.readline().strip().split()) for i in range(n))

def flip(b):
    n = len(b)
    m = len(b[0])
    return tuple(tuple(b[i][j] for i in range(n)) for j in range(m))

def toolowsquaresinrow(i, row):
    ma = max(row)
    return tuple((i,j) for j,x in enumerate(row) if x < ma)

def toolowsquares(lawn):
    toolow = []
    for i,row in enumerate(lawn):
        toolow += toolowsquaresinrow(i, row)
    return set(toolow)

def flipsquares(squares):
    return set(tuple((j,i) for i,j in squares))

def possible(lawn):
    s1 = toolowsquares(lawn)
    s2 = flipsquares(toolowsquares(flip(lawn)))
    return not s1.intersection(s2)

case = 1
infile = 'B-large.in' 
outfile = infile+'.out'
of = open(outfile, 'w')
for lawn in readinput(infile):
    verdict = 'YES' if possible(lawn) else 'NO'
    of.write("Case #%i: %s\n" % (case, verdict))
    case += 1

