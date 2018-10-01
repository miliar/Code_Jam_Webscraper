def solve(R, C, B):
    used = set()
    T = [list(row) for row in B]

    for r in range(R):
        for c in range(C):
            d = T[r][c]
            if d in used or d == '?':
                continue

            used.add(d)

            t = r
            while t-1 >= 0 and T[t-1][c] == '?':
                t -= 1
                T[t][c] = d

            b = r
            while b+1 < R and T[b+1][c] == '?':
                b += 1
                T[b][c] = d

            p = c + 1
            while p < C and not any(T[q][p] != '?' for q in range(t, b+1)):
                for q in range(t, b+1):
                    T[q][p] = d
                p += 1

            p = c - 1
            while p >= 0 and not any(T[q][p] != '?' for q in range(t, b+1)):
                for q in range(t, b+1):
                    T[q][p] = d
                p -= 1

    notDone = any(any(d == '?' for d in row) for row in T)
    if not notDone:
        return T

    used = set()
    T = [list(row) for row in B]


    for r in range(R):
        for c in range(C):
            d = T[r][c]
            if d in used or d == '?':
                continue

            used.add(d)

            t = c
            while t-1 >= 0 and T[r][t-1] == '?':
                t -= 1
                T[r][t] = d

            b = c
            while b+1 < C and T[r][b+1] == '?':
                b += 1
                T[r][b] = d

            p = r + 1
            while p < R and not any(T[p][q] != '?' for q in range(t, b+1)):
                for q in range(t, b+1):
                    T[p][q] = d
                p += 1

            p = r - 1
            while p >= 0 and not any(T[p][q] != '?' for q in range(t, b+1)):
                for q in range(t, b+1):
                    T[p][q] = d
                p -= 1

    notDone = any(any(d == '?' for d in row) for row in T)
    if not notDone:
        return T

    used = set()
    T = [list(row) for row in B]

    for r in range(R-1, -1, -1):
        for c in range(C-1, -1, -1):
            d = T[r][c]
            if d in used or d == '?':
                continue

            used.add(d)

            t = c
            while t-1 >= 0 and T[r][t-1] == '?':
                t -= 1
                T[r][t] = d

            b = c
            while b+1 < C and T[r][b+1] == '?':
                b += 1
                T[r][b] = d

            p = r + 1
            while p < R and not any(T[p][q] != '?' for q in range(t, b+1)):
                for q in range(t, b+1):
                    T[p][q] = d
                p += 1

            p = r - 1
            while p >= 0 and not any(T[p][q] != '?' for q in range(t, b+1)):
                for q in range(t, b+1):
                    T[p][q] = d
                p -= 1

    notDone = any(any(d == '?' for d in row) for row in T)
    if not notDone:
        return T

    used = set()
    T = [list(row) for row in B]

    for r in range(R-1, -1, -1):
        for c in range(C-1, -1, -1):
            d = T[r][c]
            if d in used or d == '?':
                continue

            used.add(d)

            t = r
            while t-1 >= 0 and T[t-1][c] == '?':
                t -= 1
                T[t][c] = d

            b = r
            while b+1 < R and T[b+1][c] == '?':
                b += 1
                T[b][c] = d

            p = c + 1
            while p < C and not any(T[q][p] != '?' for q in range(t, b+1)):
                for q in range(t, b+1):
                    T[q][p] = d
                p += 1

            p = c - 1
            while p >= 0 and not any(T[q][p] != '?' for q in range(t, b+1)):
                for q in range(t, b+1):
                    T[q][p] = d
                p -= 1

    return T


import sys
sys.stdin = open('A-large.in', 'rt')
sys.stdout = open('A-large.out', 'wt')

T = int(raw_input().strip())
for t in xrange(1, T+1):
    R, C = map(int, raw_input().strip().split(' '))
    print "Case #%d:" % (t)

    B = []
    for _ in range(R):
        B.append(list(raw_input().strip()))

    T = solve(R, C, B)
    for row in T:
        print ''.join(row)
