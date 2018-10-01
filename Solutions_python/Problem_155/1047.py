import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')


def zero_a(input, debug=False):
    current = 0
    friends = 0
    for i in xrange(len(input)):
        if current < i:
            friends += i - current
            current = i
        current += int(input[i])
    return friends


def read_input():
    name = 'A-large'
    f = open('%s.in' % name)
    f2 = open('%s.out' % name, 'w')
    num_cases = int(f.readline().replace('\n', ''))
    for i in xrange(num_cases):
        case_input = [a for a in f.readline().replace('\n', '').split(' ')]
        f2.write('Case #%s: %s\n' % (i + 1, zero_a(case_input[1])))
        # print case_input, zero_b(0, op)
        # import ipdb; ipdb.set_trace()


def test(expected, input, debug=False):
    print 'exp %s, got %s for %s' % (expected, zero_a(input), input)
    assert zero_a(input) == expected

read_input()

test(0, '11111')
test(1, '09')
test(2, '110011')
test(4, '110011001')
test(0, '1')
