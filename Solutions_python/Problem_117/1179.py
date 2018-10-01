import operator
n, = map(int, raw_input().split())
for case in range(1, n + 1):
    b = list()
    n, m = map(int, raw_input().split())
    for j in range(n):
        b.append(map(int, raw_input().split()))
    hasDig = set()
    for r in range(n):
        for c in range(m):
            hasDig.add(b[r][c])
    dig = sorted(list(hasDig))
    for d in dig:
        r_all, c_all = set(), set()
        for r in range(n):
            if reduce(lambda x, y: x and y, [b[r][i] == d for i in range(m)]):
                r_all.add(r)
        for c in range(m):
            if reduce(lambda x, y: x and y, [b[i][c] == d for i in range(n)]):
                c_all.add(c)
        possible = True
        for r in range(n):
            for c in range(m):
                if b[r][c] == d and (r not in r_all) and (c not in c_all):
                    possible = False
                    break
        if not possible:
            print 'Case #{}: NO'.format(case)
            break
        if len(r_all) == n or len(c_all) == m:
            print 'Case #{}: YES'.format(case)
            break
        for r in range(n):
            if r not in r_all:
                for r2 in r_all:
                    for c in range(m):
                        b[r2][c] = b[r][c]
                break
        for c in range(m):
            if c not in c_all:
                for c2 in c_all:
                    for r in range(n):
                        b[r][c2] = b[r][c]
                break
    else:
        print 'Case #{}: YES'.format(case)
