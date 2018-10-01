import sys
import numpy as np
import itertools as it

def nums_line(f):
    return np.array([int(k) for k in f.readline().strip().split()])

def main(argv=None):
    if not argv:
        argv = sys.argv[1:]
    filename = argv[0] if argv else 'test.in'

    with open(filename) as f:
        num_cases = int(f.readline())
        for case_no in xrange(1, num_cases+1):
            lawn = []
            n, m = nums_line(f)
            for i in xrange(n):
                lawn.append(nums_line(f))
            lawn = np.array(lawn)
            print "Case #{}:".format(case_no),
            if can_cut(lawn, n, m):
                print "YES"
            else:
                print "NO"

def can_cut(lawn, n, m):
    target = lawn.copy()
    heights = np.unique(lawn)
    locs = []
    for h in heights[:-1]:
        lawn[locs] = h
        locs = np.where(lawn == h)
        if not can_cut_single(set(zip(*locs)), lawn, h, n, m):
            return False
    return True

def can_cut_single(locs, lawn, h, n, m):
    while locs:
        i, j = locs.pop()
        if (lawn[i] == h).all():
            locs.difference_update(it.product((i,), xrange(m)))
        elif (lawn[:, j] == h).all():
            locs.difference_update(it.product(xrange(n), (j,)))
        else:
            return False
    return True

if __name__ == '__main__':
    main()
