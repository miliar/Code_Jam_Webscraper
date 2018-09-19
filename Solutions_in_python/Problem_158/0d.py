import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')


def zero_d(X, R, C, debug=False):
    """ True -> Richard, one domino won't fit
        False -> Gabriel, everything can work
    """
    if X == 1:
        return False  # all works
    if R * C % X != 0:
        return True  # one case will be left
    if X == 2:
        return False

    if X > max(C, R):
        return True

    if C > R:
        return zero_d(X, C, R, debug)

    trues = [(4, 4, 1), (3, 3, 1), (4, 4, 2)]
    falses = [(3, 3, 2), (3, 3, 3), (3, 4, 3), (4, 4, 3), (4, 4, 4)]
    if (X, R, C) in trues:
        return True
    if (X, R, C) in falses:
        return False

    return 'Unknown: (%s, %s, %s)' % (X, R, C)


def read_input():
    name = 'D-small-attempt0'
    f = open('%s.in' % name)
    f2 = open('%s.out' % name, 'w')
    num_cases = int(f.readline().replace('\n', ''))
    for i in xrange(num_cases):
        case_input = [int(a) for a in f.readline().replace('\n', '').split(' ')]
        answer = zero_d(*case_input)
        f2.write('Case #%s: %s\n' % (i + 1, 'RICHARD' if answer else 'GABRIEL'))
        # print case_input, zero_b(0, op)
        # import ipdb; ipdb.set_trace()


def test(expected, input, debug=False):
    print 'exp %s, got %s for %s' % (expected, zero_d(*input), input)
    assert zero_d(*input) == expected

read_input()

test(False, (1, 2, 1))
test(False, (1, 4, 4))
test(True, (4, 2, 1))
test(False, (2, 2, 2))
test(True, (2, 1, 3))
test(True, (4, 4, 1))
test(False, (3, 2, 3))
for x in range(1, 5):
    for r in range(1, 5):
        for c in range(1, 5):
            if not type(zero_d(x, r, c)) is type(True):
                print zero_d(x, r, c)
