inp = open('c:/temp/C-small-attempt0.in')
out = open('c:/temp/C-small-attempt0.out', 'w')


def isRecPair(n, m):
    N = str(n)
    M = str(m)

    l = len(M)
    for i in xrange(l):
        X = N[i:] + N[:i]
        if X == M:
            return True
    return False

n = int(inp.readline())
print n
for i in xrange(1, n+1):
    A, B = map(int, inp.readline().split())
    count = 0
    for n in xrange(A, B+1):
        for m in xrange(n+1, B+1):
            if isRecPair(n, m):
                count += 1

    out.write("Case #%d: %d\n" % (i, count))
    

inp.close()
out.close()
