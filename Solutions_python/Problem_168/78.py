def shoot(x, n, m, i, j, di, dj):
    while 0 <= i and i < n and 0 <= j  and j < m:
        i += di
        j += dj
        if 0 <= i and i < n and 0 <= j  and j < m and x[i][j] != '.':
            return True
    return False

def fail(x, n, m, i, j, di, dj):
    if shoot(x, n, m, i, j, di, dj):
        return 0
    if (shoot(x, n, m, i, j, 0, 1)
    or shoot(x, n, m, i, j, 0, -1)
    or shoot(x, n, m, i, j, 1, 0)
    or shoot(x, n, m, i, j, -1, 0)):
        return 1
    else:
        return -1

ttt = int(raw_input())
for tt in xrange(1, ttt+1):
    x = []
    ans = 0
    n, m = map(int, raw_input().strip().split())
    for i in xrange(n):
        x.append(raw_input().strip())
    for i in xrange(n):
        for j in xrange(m):
            if x[i][j] == '>':
                p = fail(x, n, m, i, j, 0, 1)
                if p == -1:
                    ans = -1
                elif ans != -1:
                    ans += p
            elif x[i][j] == '<':
                p = fail(x, n, m, i, j, 0, -1)
                if p == -1:
                    ans = -1
                elif ans != -1:
                    ans += p
            elif x[i][j] == 'v':
                p = fail(x, n, m, i, j, 1, 0)
                if p == -1:
                    ans = -1
                elif ans != -1:
                    ans += p
            elif x[i][j] == '^':
                p = fail(x, n, m, i, j, -1, 0)
                if p == -1:
                    ans = -1
                elif ans != -1:
                    ans += p
    if ans == -1:
        print 'Case #%d: IMPOSSIBLE' % tt
    else:
        print 'Case #%d: %d' % (tt, ans)