
import sys
from itertools import permutations
from copy import copy

def cost(l, r):
    c = 0
    i = r - 1
    l_len = len(l)
    while i >= 0 and l[i] is not None:
        c += 1
        i -= 1
    i = r + 1
    while i < l_len and l[i] is not None:
        c += 1
        i += 1
    return c

def total_cost(ocells, releases):
    tc = 0
    cells = copy(ocells)
    for release in releases:
        idx = release - 1
        tc += cost(cells, idx)
        cells[idx] = None
    return tc

def iso_score(ol, r, cells):
    l = copy(ol)
    l.remove(r)
    l.append(cells)
    l.append(1)
    return min(abs(r - x) for x in l)

with open(sys.argv[1]) as input:
    cases = input.readline().strip()
    for i in xrange(int(cases)):
        cells_num, r = input.readline().strip().split(' ')
        cells_num = int(cells_num)
        releases = map(int, input.readline().strip().split(' ')[:int(r)])
        cells = range(cells_num)

        #c = total_cost(cells, sorted(releases, key=lambda r: iso_score(releases, r, cells_num), reverse=True))
        c = min(total_cost(cells, r) for r in permutations(releases))

        print "Case #%s: %s" % (i+1, c)

