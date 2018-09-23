
def boundaries(c, xy, grid):
    xmin, ymin = xy
    xmax, ymax = xy

    ymin -= 1
    while ymin >= 0 and grid[ymin][xmin] == '?':
        ymin -= 1
    ymin += 1

    ymax += 1
    while ymax < len(grid) and grid[ymax][xmin] == '?':
        ymax += 1

    xmin -= 1
    flag = True
    while xmin >= 0 and flag:
        for j in range(ymin, ymax):
            if grid[j][xmin] != '?':
                flag = False
                break
        if flag:
            xmin -= 1
    xmin += 1

    xmax += 1
    flag = True
    while xmax < len(grid[0]) and flag:
        for j in range(ymin, ymax):
            if grid[j][xmax] != '?':
                flag = False
                break
        if flag:
            xmax += 1

    return xmin, xmax, ymin, ymax

def flood(init, xmin, xmax, ymin, ymax, grid):
    for j in xrange(ymin, ymax):
        for i in xrange(xmin, xmax):
            grid[j][i] = init

def process(grid):
    inits = {}
    for j in xrange(len(grid)):
        for i in xrange(len(grid[0])):
            if grid[j][i] != '?':
                inits[grid[j][i]] = (i, j)
    for c in inits:
        xmin, xmax, ymin, ymax = boundaries(c, inits[c], grid)
        flood(c, xmin, xmax, ymin, ymax, grid)

def do_case(i):
    R, C = map(int, raw_input().split())
    grid = []
    for j in xrange(R):
        grid.append(list(raw_input()))
    process(grid)
    print "Case #{}:".format(i+1)
    for row in grid:
        print ''.join(row)

def main():
    T = int(raw_input())
    for i in xrange(T):
        do_case(i)

main()
