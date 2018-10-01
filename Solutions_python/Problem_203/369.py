T = int(raw_input())

for case in range(T):

    R,C = map(int, raw_input().split())

    sup = dict()
    sdown = dict()
    sleft = dict()
    sright = dict()

    tomod = 0

    grid = []
    for r in range(R):
        row = raw_input()
        grid.append([c for c in row])
        for c in range(C):
            if row[c] != '?':
                if row[c] in sup:
                    sup[row[c]] = min(sup[row[c]], r)
                else:
                    sup[row[c]] = r
                if row[c] in sdown:
                    sdown[row[c]] = max(sdown[row[c]], r)
                else:
                    sdown[row[c]] = r
                if row[c] in sleft:
                    sleft[row[c]] = min(sleft[row[c]], c)
                else:
                    sleft[row[c]] = c
                if row[c] in sright:
                    sright[row[c]] = max(sright[row[c]], c)
                else:
                    sright[row[c]] = c
            else:
                tomod += 1
    moded = 0

    for k in sup.keys():
        for rr in range(sup[k], sdown[k]+1):
            for cc in range(sleft[k], sright[k]+1):
                if grid[rr][cc] == '?':
                    moded += 1
                grid[rr][cc] = k

    for k in sup.keys():
        while sleft[k] > 0:
            if all([grid[rr][sleft[k]-1] == '?' for rr in range(sup[k], sdown[k]+1)]):
                for rr in range(sup[k], sdown[k]+1):
                    grid[rr][sleft[k]-1] = k
                sleft[k] -= 1
            else:
                break
        while sright[k] < C-1:
            if all([grid[rr][sright[k]+1] == '?' for rr in range(sup[k], sdown[k]+1)]):
                for rr in range(sup[k], sdown[k]+1):
                    grid[rr][sright[k]+1] = k
                sright[k] += 1
            else:
                break
        while sup[k] > 0:
            if all([grid[sup[k]-1][cc] == '?' for cc in range(sleft[k], sright[k]+1)]):
                for cc in range(sleft[k], sright[k]+1):
                    grid[sup[k]-1][cc] = k
                sup[k] -= 1
            else:
                break
        while sdown[k] < R-1:
            if all([grid[sdown[k]+1][cc] == '?' for cc in range(sleft[k], sright[k]+1)]):
                for cc in range(sleft[k], sright[k]+1):
                    grid[sdown[k]+1][cc] = k
                sdown[k] += 1
            else:
                break



    print "Case #{0}:".format(case+1)
    for g in grid:
        print ''.join(g)
