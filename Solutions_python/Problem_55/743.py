import sys
from itertools import cycle, islice, count

def fill_cars(k, groups):
    ngroup = len(groups)
    groups = cycle(groups)

    c = 0
    g = 0
    while True:
        c = g
        for i in xrange(ngroup):
            g = next(groups)
            if c + g > k:
                break
            c += g
            g = 0
        yield c

def splits(s, func):
    return list(map(func, s.strip().split()))

if __name__ == "__main__":
    with open(sys.argv[1]) as fp:
        t = int(next(fp))
        for i in range(t):
            r, k, n = splits(next(fp), int)
            groups = splits(next(fp), int)
            assert len(groups) == n

            cars = fill_cars(k, groups)
            revenue = sum(islice(cars, r))
            print "Case #%d: %d" % (i+1, revenue)
