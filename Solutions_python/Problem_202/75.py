
import sys
import math

ntests = int(sys.stdin.readline())

for ncase in range(ntests):
    N, M = map(int, sys.stdin.readline().split(' '))
    input_str = '{0} {1}\n'.format(N, M)
    grid = [['.' for i in range(N)] for j in range(N)]
    orig_grid = [['.' for i in range(N)] for j in range(N)]
    for i in range(M):
        line = sys.stdin.readline()
        input_str += line + '\n'
        a, r, c = line.split(' ')
        grid[int(r) - 1][int(c) - 1] = a
        orig_grid[int(r) - 1][int(c) - 1] = a
    
    rGrid = [[a in ['x', 'o'] for a in row] for row in grid]
    bGrid = [[a in ['+', 'o'] for a in row] for row in grid]

    additions = {}

    def logGrid(g = grid):
        print('grid:')
        for r in g:
            print(''.join(r))
        print()

    # logGrid()

    def addItem(r, c, v):
        other = '+' if v == 'x' else 'x'
        if grid[r][c] == '.':
            grid[r][c] = v
            additions[(r, c)] = v
        elif grid[r][c] == other:
            grid[r][c] = 'o'
            additions[(r, c)] = 'o'

    while True:
        # logGrid()
        emptyRow = None
        emptyCol = None
        for i in range(N):
            isEmptyRow = True
            isEmptyCol = True
            for j in range(N):
                if rGrid[i][j]: isEmptyRow = False
                if rGrid[j][i]: isEmptyCol = False
            if isEmptyRow: emptyRow = i
            if isEmptyCol: emptyCol = i
        # print(emptyRow, emptyCol)
        if emptyRow is None: break
        rGrid[emptyRow][emptyCol] = True
        addItem(emptyRow, emptyCol, 'x')

    # logGrid()

    def distToEdge(r, c):
        return min(N - r - 1, N - c - 1, r, c)
    
    def canPlaceB(r0, c0):
        for r1 in range(N):
            for c1 in range(N):
                if ((r0 + c0 == r1 + c1) or (r0 - c0 == r1 - c1)) and bGrid[r1][c1]: return False
        return True

    markedGrid = [[False for c in row] for row in grid]

    def tryMark(r, c):
        if 0 <= r < N and 0 <= c < N: markedGrid[r][c] = True

    def markLocation(r, c):
        bGrid[r][c] = True
        addItem(r, c, '+')
        for i in range(-N+1, N):
            tryMark(r + i, c + i)
            tryMark(r + i, c - i)

    for i in range(N):
        for j in range(N):
            if bGrid[i][j]: markLocation(i, j)

    for d in range((N // 2) + 1):
        for i in range(d, N-d):
            for j in range(d, N-d):
                if distToEdge(i, j) != d or markedGrid[i][j]: continue
                markLocation(i, j)

    def value(v):
        vals = { '+': 1, 'x': 1, 'o': 2 }
        return 0 if v not in vals else vals[v]

    # logGrid()

    total = sum(sum(value(a) for a in row) for row in grid)

    expected = 2 * N + max(0, N - 2)

    '''
    if total != expected:
        print(input_str, file=sys.stderr)
        logGrid(orig_grid)
        logGrid()
        raise BaseException("total {0} not the same as expected {1}".format(total, expected))
    '''

    result = '{0} {1}'.format(total, len(additions))

    print('Case #{0}: {1}'.format(ncase + 1, result), file=sys.stderr)
    print('Case #{0}: {1}'.format(ncase + 1, result))
    for (r, c), v in sorted(additions.items()):
        print('{0} {1} {2}'.format(v, r + 1, c + 1))
