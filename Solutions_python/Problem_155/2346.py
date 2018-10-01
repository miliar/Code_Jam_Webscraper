import sys


def solve(case, esses):
    y = 0
    standing = 0
    for j, s in enumerate(esses):
        if standing < j:
            y += (j - standing)
            standing = j
        standing += s
    print 'Case #%d: %d' % (case, y)


def main():
    input = [line.strip() for line in sys.stdin.readlines()]
    T = input.pop(0)
    input = [line.split(' ') for line in input]
    input = [map(int, list(line[1])) for line in input]
    for i, esses in enumerate(input):
        solve(i + 1, esses)


if __name__ == '__main__':
    main()
