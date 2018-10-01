import sys

def fill(cake, r, c, initial):
    minr = r
    minc = c

    maxr = r
    maxc = c


    for i in xrange(len(cake)):
        if initial in cake[i]:
            maxr = max(maxr, i)
            minr = min(minr, i)

            idx = "".join(cake[i]).rfind(initial)

            maxc = max(maxc, idx)
            minc = max(minc, idx)

    h = maxr - minr + 1
    w = maxc - minc + 1

    for i in xrange(h):
        for j in xrange(w):
            cake[minr + i][minc + j] = initial

    for i in xrange(minr - 1, -1, -1):
        good = True
        for j in xrange(minc, maxc + 1):
            if cake[i][j] != '?' and cake[i][j] != initial:
                good = False
                break
        if good:
            for j in xrange(minc, maxc + 1):
                cake[i][j] = initial
            minr = i
        else:
            break

    for i in xrange(maxr + 1, len(cake)):
        good = True
        for j in xrange(minc, maxc + 1):
            if cake[i][j] != '?' and cake[i][j] != initial:
                good = False
                break

        if good:
            for j in xrange(minc, maxc + 1):
                cake[i][j] = initial

            maxr = i
        else:
            break

    for j in xrange(minc - 1, -1, -1):
        good = True
        for i in xrange(minr, maxr + 1):
            if cake[i][j] != '?' and cake[i][j] != initial:
                good = False
                break
        if good:
            for i in xrange(minr, maxr + 1):
                cake[i][j] = initial

            minc = i
        else:
            break

    for j in xrange(maxc + 1,len(cake[0])):
        good = True
        for i in xrange(minr, maxr + 1):
            if cake[i][j] != '?' and cake[i][j] != initial:
                good = False
                break
        if good:
            for i in xrange(minr, maxr + 1):
                cake[i][j] = initial

            maxc = i
        else:
            break


T = int(raw_input())

for tc in xrange(1, T + 1):
    r, c = map(int, raw_input().split())
    cake = []

    for i in xrange(r):
        line = raw_input().strip()
        cake.append(list(line))
    done = set()
    for i in xrange(r):
        for j in xrange(c):
            if cake[i][j] == '?':
                continue
            if cake[i][j] in done:
                continue

            done.add(cake[i][j])

            fill(cake, i, j, cake[i][j])

    print "Case #%d:" % (tc, )

    for i in cake:
        print "".join(i)

