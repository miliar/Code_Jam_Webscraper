import re
T = int(raw_input().strip())
CHILDREN = re.compile('[A-Z]')

for t in xrange(T):
    R, C = map(int, raw_input().strip().split(' '))
    grids = [None] * R

    for i in xrange(R):
        grids[i] = raw_input().strip()
        if '?' not in grids[i]:
            continue
        matches = CHILDREN.search(grids[i])
        if matches is None:
            if i > 0:
                grids[i] = grids[i - 1]
            else:
                continue
        else:
            child = matches.group(0)
            _grid = [None] * C
            for j in xrange(C):
                if grids[i][j] == '?':
                    _grid[j] = child
                else:
                    child = grids[i][j]
                    _grid[j] = child
            grids[i] = ''.join(_grid)

    # Reprocess any missing ?
    for i in xrange(R):
        g = grids[i]
        if '?' not in g:
            continue

        for j in xrange(i + 1, R):
            if '?' in grids[j]:
                continue
            grids[i] = grids[j]
            break

    print 'Case #%d:' % (t + 1)
    for i in xrange(R):
        print grids[i]