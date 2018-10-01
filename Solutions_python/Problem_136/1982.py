def solve(C, F, X):
    ret = X / 2.0
    csum = 0.0
    for num_farms in xrange(200000):
        csum += C / (2.0 + num_farms * F)
        ret = min(ret, csum + X / (2.0 + F * (num_farms + 1)))

    return ret


def main():
    num_cases = int(raw_input())
    for case in xrange(num_cases):
        (C, F, X) = map(float, raw_input().split())
        print "Case #%d: %.7lf" % (case + 1, solve(C, F, X))

if __name__ == '__main__':
    main()
