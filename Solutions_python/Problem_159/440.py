import sys


def method1(xs):
    accum = 0
    for i in xrange(len(xs) - 1):
        accum += max(0, xs[i] - xs[i + 1])
    return accum


def method2(xs):
    max_slope = 0
    for i in xrange(len(xs) - 1):
        slope = xs[i] - xs[i + 1]
        if slope > max_slope:
            max_slope = slope
    if max_slope == 0:
        return 0
    accum = 0
    for x in xs[:-1]:
        accum += min(max_slope, x)
    return accum


if __name__ == '__main__':
    case_count = int(sys.stdin.readline())

    for i in xrange(case_count):
        _ = sys.stdin.readline()
        xs = map(int, sys.stdin.readline().split(' '))
        print 'Case #{}: {} {}'.format(i + 1, method1(xs), method2(xs))
