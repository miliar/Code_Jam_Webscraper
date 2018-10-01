import psyco
psyco.full()

def get_neighbors(x, y, X, Y):
    nb = []

    # north, west, east, south
    if y > 0: nb += [(x, y-1)]
    if x > 0: nb += [(x-1, y)]
    if x < X - 1: nb += [(x+1, y)]
    if y < Y - 1: nb += [(x, y+1)]

    return nb

def solve():
    for case in xrange(input()):
        Y, X = [int(s) for s in raw_input().split()]

        # basin map
        bmap = [[None] * X for _ in xrange(Y)]

        # reverse flow map adjacency list
        fmap = [[[] for _2 in xrange(X)] for _ in xrange(Y)]

        # elevation map
        emap = []
        for y in xrange(Y):
            emap += [[int(s) for s in raw_input().split()]]

        sinks = []
        for y in xrange(Y):
            for x in xrange(X):
                nb = get_neighbors(x, y, X, Y)

                if nb:
                    lowest = min(emap[ny][nx] for nx, ny in nb)
                    if lowest < emap[y][x]:
                        for nx, ny in nb:
                            if emap[ny][nx] == lowest:
                                fmap[ny][nx] += [(x, y)]
                                break
                    else:
                        bmap[y][x] = len(sinks)
                        sinks += [(x,y)]
                else:
                    bmap[y][x] = len(sinks)
                    sinks += [(x,y)]

        q = [(x, y, idx) for idx, (x, y) in enumerate(sinks)]
        while q:
            ux, uy, basin = q[0]
            q = q[1:]

            for nx, ny in fmap[uy][ux]:
                assert bmap[ny][nx] is None

                bmap[ny][nx] = basin
                q += [(nx, ny, basin)]

        print 'Case #%d:' % (case + 1)

        labels = {}
        for y in xrange(Y):
            row = []
            for x in xrange(X):
                assert bmap[y][x] is not None

                if not bmap[y][x] in labels:
                    labels[bmap[y][x]] = chr(ord('a') + len(labels))

                row += [labels[bmap[y][x]]]
            print ' '.join(row)

solve() # so that psyco can do its magic
