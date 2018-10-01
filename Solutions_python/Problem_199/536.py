import sys

def solve(line, size):
    """
    >>> solve('---+-++-', 3)
    3
    >>> solve('+++++', 4)
    0
    >>> solve('-+-+-', 4)
    'IMPOSSIBLE'
    >>> solve('----', 4)
    1
    >>> solve('----', 2)
    2
    >>> solve('----', 3)
    'IMPOSSIBLE'
    """
    line = [c == '+' for c in line]
    flips = [0]
    def flip(offset):
        assert offset + size <= len(line)
        line[offset:offset + size] = [not c for c in line[offset:offset + size]]
        flips[0] += 1
    for idx in xrange(len(line) - size + 1):
        if not line[idx]:
            flip(idx)
    if all(line):
        return flips[0]
    else:
        return 'IMPOSSIBLE'


def main():
    count = int(next(sys.stdin).strip())
    for case in xrange(1, count + 1):
        line, size = next(sys.stdin).split()
        print 'Case #{}: {}'.format(case, solve(line, int(size)))


if __name__ == '__main__':
    main()
