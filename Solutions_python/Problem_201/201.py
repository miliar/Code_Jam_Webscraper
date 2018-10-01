#!/usr/bin/python
import math
import sys


def solve(n, k, case_number):
    level = len(bin(k)) - 3
    section = int(math.pow(2, level))
    available = n - (section - 1)
    size = int(available / section)
    remain = available - (size * section)
    if k - section < remain:
        size += 1

    minimum = int((size - 1) / 2)
    maximum = minimum + (0 if (size - 1) % 2 == 0 else 1)
    print("Case #%d: %d %d" % (case_number, maximum, minimum))


def main():
    r = sys.stdin
    if len(sys.argv) > 1:
        r = open(sys.argv[1], 'r')

    total_cases = r.readline()
    for case_number in range(1, int(total_cases) + 1):
        n, k = map(int, r.readline().strip().split(' '))

        solve(n, k, case_number)


if __name__ == "__main__":
    main()
