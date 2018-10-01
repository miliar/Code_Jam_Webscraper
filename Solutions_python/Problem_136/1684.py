import sys


def cases(filename):
    with open(filename, 'r') as f:
        t = int(f.readline().strip())
        for _ in range(t):
            yield tuple(map(float, f.readline().strip().split()))


def solve(c, f, x):

    def time(numfarms):
        farmtime = sum(c / (2.0 + i * f) for i in range(numfarms))
        return farmtime + x / (2.0 + numfarms * f)

    return min(map(time, range(int(x / c) + 1)))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: {} filename'.format(sys.argv[0]))
        sys.exit(1)
    sys.setrecursionlimit(10000)
    for i, case in enumerate(cases(sys.argv[1]), 1):
        print('Case #{}: {:.7f}'.format(i, solve(*case)))
