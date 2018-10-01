import sys
NAME = None
#NAME = "-small-attempt"
#NAME = "-large"

def balanced(a, si, sj, D, k):
    x = (0, 0)
    y = (0, 0)
    c = k - 1
    for i in range(k):
        for j in range(k):
            if (i == 0 or i == k - 1) and (j == 0 or j == k - 1):
                continue
            m = ord(a[si + i][sj + j]) - ord('0') + D
            x = (x[0] + m * j * 2, x[1] + m)
            y = (y[0] + m * i * 2, y[1] + m)
    return x[0] == x[1] * c and y[0] == y[1] * c

def test(a, N, M, D, k):
    for i in range(N - k + 1):
        for j in range(M - k + 1):
            if balanced(a, i, j, D, k):
                return True
    return False

def getMagicWord():
    N = nextToken(int)
    M = nextToken(int)
    D = nextToken(int)
    a = []
    for i in range(N):
        a.append(nextToken())
    for k in range(min(N, M), 2, -1):
        if test(a, N, M, D, k):
            return str(k)
    return "IMPOSSIBLE"

################################################
################################################
def nextToken(func = None):
    c = ""
    while fin:
        c = fin.read(1)
        if not c.isspace():
            break
    res = "" + c
    while fin:
        c = fin.read(1)
        if c.isspace():
            break
        res += c
    if func:
        return func(res)
    else:
        return res

def nextLine():
    if fin:
        return fin.readline()
    else:
        return ""

if NAME:
    fin, fout = open(NAME + ".in", "r"), open(NAME + ".out", "w")
else:
    fin, fout = sys.stdin, sys.stdout

#########################
for testNum in range(nextToken(int)):
    print("Case #%d: %s" % (testNum + 1, getMagicWord()))
