import itertools
import sys

inp = sys.stdin

def solve_slow(cs):
    if len(cs) < 2:
        return None
    cs = tuple(cs)
    idxs = range(len(cs))
    powerset = itertools.chain.from_iterable(itertools.combinations(idxs, r) for r in xrange(len(idxs) + 1))
    best = -1
    for s in powerset:
        if not len(s):
            continue
        if len(s) == len(cs):
            continue
        seans_idxs = set(s)
        for_sean = []
        for_patrick = []
        for i in xrange(len(cs)):
            if i in seans_idxs:
                for_sean.append(cs[i])
            else:
                for_patrick.append(cs[i])
        if reduce(lambda x, y: x^y, for_sean) == reduce(lambda x, y: x^y, for_patrick):
            best = max(sum(for_sean), best)
    if best != -1:
        return best

def solve_fast(cs):
    if len(cs) < 2:
        return None
    if reduce(lambda x, y: x^y, cs) != 0:
        return None
    return sum(cs) - min(cs)

T = int(inp.readline())
for t in xrange(1, T + 1):
    N = int(inp.readline())
    cs = map(int, inp.readline().split())
    res = solve_fast(cs)
    print 'Case #%d: %s' % (t, res or 'NO')

