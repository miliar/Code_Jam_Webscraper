__author__ = 'octav'


def solve(size, values):
    size = int(size)
    counter, s = 0, int(values[0])
    for i in xrange(1, size + 1):
        values_i = int(values[i])
        if s < i:
            difference = i - s
            s += difference
            counter += difference
        s += values_i
    return counter


def main():
    with open('in.txt') as in_file, open('out.txt', 'w') as out_file:
        tests_number = int(in_file.readline())
        for test_number in xrange(1, tests_number + 1):
            size, values = in_file.readline().split()
            result = solve(size, values)
            out_file.write('Case #%s: %s\n' % (test_number, result))


if __name__ == '__main__':
    main()
