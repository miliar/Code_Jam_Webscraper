import sys

res = {True: 'YES', False: 'NO'}

cases = int(sys.stdin.readline())
for case in xrange(cases):
    e = sys.stdin.readline().split()
    l = []
    row = int(e[0])
    col = int(e[1])

    for r in xrange(row):
        l.append(map(int, sys.stdin.readline().split()))

    r = map(max, l)
    c = map(max, zip(*l))

    valid = all([l[i][j] == min(r[i], c[j])
                 for i in xrange(row)
                 for j in xrange(col)])

    print 'Case #%s: %s' % (case+1, res[valid])
