def expandColumn(grid, j, k):
    newgrid = grid
    element = newgrid[j][k]
    i = k+1
    while i < len(grid[0]) and newgrid[j][i] == '?':
        newgrid[j][i] = element
        i += 1
    i = k-1
    while i >= 0 and newgrid[j][i] == '?':
        newgrid[j][i] = element
        i -= 1
    return newgrid

def expandRow(grid, j, k):
    newgrid = grid
    element = newgrid[j][k]
    i = j+1
    while i < len(grid) and newgrid[i][k] == '?':
        newgrid[i][k] = element
        i += 1
    i = j-1
    while i >= 0 and newgrid[i][k] == '?':
        newgrid[i][k] = element
        i -= 1
    return newgrid

def printGrid(grid):
    for i in xrange(len(grid)):
        print ''.join(grid[i])

t = int(raw_input())
for i in xrange(1, t + 1):
    n, m = [s.strip() for s in raw_input().split(" ")]
    n = int(n)
    m = int(m)
    cakegrid = []
    expandedCol = []
    expandedRow = []
    for j in xrange(n):
        cakegrid.append(list(raw_input()))
    for j in xrange(n):
        for k in xrange(m):
            if cakegrid[j][k] != '?':
                if cakegrid[j][k] not in expandedRow and cakegrid[j][k] not in expandedCol:
                    if k+1 < m and cakegrid[j][k+1] == '?' or k-1 >= 0 and cakegrid[j][k-1] == '?':
                        expandedCol.append(cakegrid[j][k])
                        cakegrid = expandColumn(cakegrid, j, k)
                    elif j+1 < n and cakegrid[j+1][k] == '?' or j-1 >= 0 and cakegrid[j-1][k] == '?':
                        expandedRow.append(cakegrid[j][k])
                        cakegrid = expandRow(cakegrid, j, k)
    used = []
    more = False
    for j in xrange(n):
        for k in xrange(m):
            if cakegrid[j][k] == '?':
                more = True
                break
    if more:
        for j in xrange(n):
            for k in xrange(m):
                if cakegrid[j][k] != '?':
                    if cakegrid[j][k] not in used and cakegrid[j][k] in expandedCol:
                        used.append(cakegrid[j][k])
                        ctr = k
                        count = 0
                        while ctr < len(cakegrid[0]) and cakegrid[j][ctr] == cakegrid[j][k]:
                            count += 1
                            ctr += 1
                        ctr = k
                        for l in xrange(count):
                            if j-1 >= 0:
                                if cakegrid[j-1][ctr] == '?':
                                    up = True
                                if cakegrid[j-1][ctr] != '?':
                                    up = False
                                    break
                                ctr += 1
                            else:
                                up = False
                                break
                        ctr = k
                        for l in xrange(count):
                            if j+1 < n:
                                if cakegrid[j+1][ctr] == '?':
                                    down = True
                                if cakegrid[j+1][ctr] != '?':
                                    down = False
                                    break
                                ctr += 1
                            else:
                                down = False
                                break
                        if up:
                            ctr = k
                            for l in xrange(count):
                                cakegrid[j-1][ctr] = cakegrid[j][k]
                                ctr+=1
                        if down:
                            ctr = k
                            for l in xrange(count):
                                cakegrid[j+1][ctr] = cakegrid[j][k]
                                ctr+=1
    print "Case #{}:".format(i)
    printGrid(cakegrid)
