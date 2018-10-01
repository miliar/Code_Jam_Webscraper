basename = "C-small-attempt0"
infile = file(basename + ".in")
outfile = open(basename + ".out", "w")

def readgrid():
    R = int(infile.readline())
    G = [[0] * 101 for x in xrange(101)]
    for r in xrange(R):
        x1, y1, x2, y2 = map(int, infile.readline().split())
        assert x2 >= x1
        assert y2 >= y1
        for x in xrange(x1, x2 + 1):
            for y in xrange(y1, y2 + 1):
                G[y][x] = 1
    return G

def printgrid(G):
    outfile.write("\n".join([" ".join(["%d" % c for c in row]) for row in G]) + "\n")
    outfile.write("\n")

def step(G):
    for row_ix in xrange(len(G) - 1, -1, -1):
        for col_ix in xrange(len(G[0]) - 1, -1, -1):
            if G[row_ix][col_ix] == 1:
                new = 1
                if row_ix == 0 or col_ix == 0:
                    new = 0
                elif G[row_ix-1][col_ix] == 0 and G[row_ix][col_ix-1] == 0:
                    new = 0
                G[row_ix][col_ix] = new
            else:
                if row_ix > 0 and col_ix > 0:
                    if G[row_ix-1][col_ix] == 1 and G[row_ix][col_ix-1] == 1:
                        G[row_ix][col_ix] = 1

def has_bacteria(G):
    return sum([sum(row) for row in G]) > 0

def runcase(casenum):
    grid = readgrid()

    t = 0
    while has_bacteria(grid):
        #printgrid(grid)
        step(grid)
        t += 1

    #printgrid(grid)
    
    outfile.write("Case #%d: %d\n" % (casenum, t))
    
C = int(infile.readline())
for c in range(1, C+1):
    runcase(c)
