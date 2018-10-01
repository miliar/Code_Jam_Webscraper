import sys

if len(sys.argv) > 1:
    sys.stdin = open(sys.argv[1])


def type2int(t):
    return ".+xo".index(t)


def int2type(i):
    return ".+xo"[i]



def add_model(stage, bits, row, col):
    global score
    score += (bits+1)/2

    stage[row][col] |= bits


    if bits & 1:
        diag1[row+col] = False
        diag2[N-col-1+row] = False

    if bits & 2:
        cols[col] = False
        rows[row] = False


def iterate_diagonals(N):
    for i in xrange(N-1):
        yield i, xrange(0, i+1)
        yield 2*N - 2 - i, xrange(N-i-1, N)
    yield N-1, xrange(0, N)

for test in range(input()):
    print "Case #{}:".format(test+1),

    N, M = map(int, raw_input().split())

    initialStage = [[0]*N for i in xrange(N)]

    rows = [True] * N
    cols = [True] * N

    diag1 = [True] * (2*N-1)
    diag2 = [True] * (2*N-1)

    score = 0

    for model in xrange(M):
        s = raw_input().split()
        t = type2int(s[0])
        row, col = int(s[1])-1, int(s[2])-1
        add_model(initialStage, t, row, col)

    newStage = [[initialStage[r][c] for c in xrange(N)] for r in xrange(N)]

    for diag, row_range in iterate_diagonals(N):
        for row in row_range:
            col = diag - row

            if cols[col] and rows[row]:
                add_model(newStage, 2, row, col)

            if diag1[diag] and diag2[N-col-1+row]:
                add_model(newStage, 1, row, col)

    newModels = 0
    for row in xrange(N):
        for col in xrange(N):
            if initialStage[row][col] != newStage[row][col]:
                newModels += 1

    print score, newModels

    for row in xrange(N):
        for col in xrange(N):
            if initialStage[row][col] != newStage[row][col]:
                print int2type(newStage[row][col]), row+1, col+1

