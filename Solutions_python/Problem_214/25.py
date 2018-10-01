if 1:
    from sys import *
    from functools import *
    from collections import *
    from itertools import *
    from functools import *
    from heapq import *
    xr = xrange

    def print_args(*args, **kwargs):
        return ','.join(value for value in [','.join(map(repr, args)),','.join("%s=%s" % (k, repr(v)) for k, v in kwargs.items())] if value)

    def print_result(before=False, after=True):
        def fc(func):
            @wraps(func)
            def f(*args, **kwargs):
                if before:
                    print "%s(%s)"      % (func.__name__, print_args(*args, **kwargs))
                r = func(*args, **kwargs)
                if after:
                    print "%s(%s) = %s" % (func.__name__, print_args(*args, **kwargs), r)
                return r
            return f
        return fc

    def memoize(function):
        memo = {}
        @wraps(function)
        def f(*args):
            key = args
            if key not in memo:
                memo[key] = function(*args)
                if not (len(memo) & 32767):
                    print >>stderr, "memo", function.__name__, len(memo)
            return memo[key]
        f.memo = memo
        return f

    def line():
        return raw_input().strip()

    def parts(f=int):
        return map(f, line().split())

    def qparts(f=int):
        data = line().split()
        return data[0], map(f, data[1:])

for cas in xrange(1,1+input()):
    ans = 0


    r, c = parts()
    grid = []

    for i in xrange(r):
        grid.append(list(line()))

    def good(i, j):
        return 0 <= i < r and 0 <= j < c and grid[i][j] != '#'

    # pair = {
    #     '/': {
    #         (0, 1): ()
    #     },
    #     '\\': pairs([
    #         ])
    # }

    # def turn(d, x):
    #     if x == '.': return d
    #     if x == '/': 

    def solve():
        index = lambda i, j: i*c + j
        def add((a, b), (c, d)):
            return a + c, b + d
        def try_beam(i, j, x):
            ds = [(0, -1), (0, 1)] if x == '-' else [(-1, 0), (1, 0)]
            starts = [(add((i, j), d), d) for d in ds]
            s = set()
            while starts:
                (i, j), d = starts.pop()
                if not good(i, j): continue
                if grid[i][j] in '-|': return
                s.add(index(i, j))
                # d = turn(d, grid[i][j])
                starts.append((add((i, j), d), d))
            return s

        bads = 0
        beamses = []
        goodses = []
        for i in xrange(r):
            for j in xrange(c):
                if grid[i][j] == '.': bads |= 1 << index(i, j)
                if grid[i][j] in '-|':
                    beams = []
                    for x in '-|':
                        s = try_beam(i, j, x)
                        if s is not None:
                            beams.append((sum(1 << v for v in s), (i, j, x)))
                    if not beams: return
                    if len(beams) == 1:
                        goodses += beams
                    else:
                        beamses.append(beams)

        def write((i, j, x)):
            grid[i][j] = x
        for g, data in goodses:
            bads -= g
            write(data)

        # print bads
        # print beamses
        @memoize
        def subok(i, topak):
            if i == len(beamses):
                return not topak

            for s, data in beamses[i]:
                if subok(i + 1, topak & ~s):
                    write(data)
                    return True

            return False


        return subok(0, bads)


    if solve():
        print "Case #%s: POSSIBLE" % cas
        for row in grid:
            print ''.join(row)
    else:
        print "Case #%s: IMPOSSIBLE" % cas
