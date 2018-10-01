
filename = 'C-large'

fin = open(filename + '.in')
fout = open(filename + '.out', 'w')
cases = int(fin.readline().strip())
for case in xrange(1, cases + 1):
    r, k, n = [int(x) for x in fin.readline().strip().split()]
    g = [int(x) for x in fin.readline().strip().split()]
    s = []
    nextg = []
    for i in xrange(n):
        s.append(0)
        x = i
        gs = 0
        while s[i] + g[x] <= k and gs < n:
            s[i] += g[x]
            x = (x + 1) % n
            gs += 1
        nextg.append(x)
    table = [0] * n
    y = x = gc = 0
    rc = [0]
    while not table[x]:
        rc.append(rc[gc] + s[x])
        gc += 1
        table[x] = gc
        x = nextg[x]
    if r <= gc:
        ans = rc[r]
    else:
        r -= gc
        ans = rc[gc]
        c = gc - table[x] + 1
        ans += ((rc[gc] - rc[table[x] - 1]) * (r / c) +
                rc[table[x] - 1 + r % c] - rc[table[x] - 1])
    fout.write('Case #%d: %d\n' % (case, ans))
fin.close()
fout.close()
