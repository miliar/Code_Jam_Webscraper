from fractions import gcd

def gap(years):
    xs = sorted(years)
    ds = [a-b for a, b in zip(xs[1:], xs)]
    result = ds.pop()
    while ds:
        result = gcd(result, ds.pop())
    return result

def next_event(year, cycle):
    return year % cycle
    #while year < 0:
    #    year += cycle
    #return year

def solve(years):
    cycle = gap(years)
    return next_event(-min(years), cycle)

if __name__ == '__main__':
    import sys
    it = iter(sys.stdin)
    next(it)
    for i, line in enumerate(it, 1):
        years = map(int, line.split()[1:])
        print 'Case #{0}: {1}'.format(i, solve(years))
