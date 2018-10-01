def solve(Smax, S):
    add = 0
    total = 0
    for idx in xrange(Smax + 1):
        cur = int(S[idx])
        if total < idx:
            add += idx - total
            total += idx - total
        total += cur
    return add

if __name__ == '__main__':
    tests = int(raw_input());
    for test_id in xrange(1, tests + 1):
        Smax, S = raw_input().split(' ')[0:2]
        print 'Case #' + str(test_id) + ': ' + str(solve(int(Smax), S))

