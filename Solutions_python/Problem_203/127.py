from collections import defaultdict


def solve(grid):
    r, c = len(grid), len(grid[0])
    processed = set()
    for i in xrange(r):
        for j in xrange(c):
            ch = grid[i][j]
            if ch != '?' and ch not in processed:
                status = horizontal(grid, ch, (i, j))
                if status == 0:
                    vertical(grid, ch, (i, j))
                processed.add(ch)
    return '\n'.join([''.join(x) for x in grid])


def horizontal(grid, ch, start):
    i, j = start
    k = j
    status = 0
    minx = maxx = j
    while k-1 >= 0 and grid[i][k-1] == '?':
        k -= 1
        minx = k
        grid[i][k] = ch
        status = 1
    k = j
    while k+1 < len(grid[0]) and grid[i][k+1] == '?':
        k += 1
        maxx = k
        grid[i][k] = ch
        status = 1
    if status == 1:
        for k in xrange(i-1, -1, -1):
            good = True
            for l in xrange(minx, maxx+1):
                if grid[k][l] != '?':
                    good = False
                    break
            if not good:
                break
            for l in xrange(minx, maxx+1):
                grid[k][l] = ch
        for k in xrange(i+1, len(grid)):
            good = True
            for l in xrange(minx, maxx+1):
                if grid[k][l] != '?':
                    good = False
                    break
            if not good:
                break
            for l in xrange(minx, maxx+1):
                grid[k][l] = ch
    return status


def vertical(grid, ch, start):
    i, j = start
    k = i
    status = 0
    miny = maxy = i
    while k-1 >= 0 and grid[k-1][j] == '?':
        k -= 1
        grid[k][j] = ch
        status = 1
    k = i
    while k+1 < len(grid) and grid[k+1][j] == '?':
        k += 1
        grid[k][j] = ch
        status = 1
    if status == 1:
        for k in xrange(j-1, -1, -1):
            good = True
            for l in xrange(miny, maxy+1):
                if grid[l][k] != '?':
                    good = False
                    break
            if not good:
                break
            for l in xrange(miny, maxy+1):
                grid[l][k] = ch
        for k in xrange(j+1, len(grid[0])):
            good = True
            for l in xrange(miny, maxy+1):
                if grid[l][k] != '?':
                    good = False
                    break
            if not good:
                break
            for l in xrange(miny, maxy+1):
                grid[l][k] = ch
    return status


if __name__ == '__main__':
    for qq in xrange(1, int(raw_input())+1):
        R, C = map(int, raw_input().split())
        grid = []
        for _ in xrange(R):
            grid.append(list(raw_input()))
        ans = solve(grid)
        print 'Case #{}:'.format(qq)
        print ans
