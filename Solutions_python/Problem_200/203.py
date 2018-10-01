#!/usr/bin/python
import sys


def is_tidy(n):
    last = 0
    for s in str(n):
        i = int(s)
        if last > i:
            return False
        last = i
    return True


def solve(n, case_number):
    nl = list(map(int, list(str(n))))
    while True:
        last = 0
        for i, x in enumerate(nl):
            if last > x:
                nl[i - 1] -= 1
                nl[i:] = [9] * (len(nl) - i)
                break
            last = x
        else:
            break

    print("Case #%d: %d" % (case_number, int("".join(map(str, nl)))))


def main():
    r = sys.stdin
    if len(sys.argv) > 1:
        r = open(sys.argv[1], 'r')

    total_cases = r.readline()
    for case_number in range(1, int(total_cases) + 1):
        n = int(r.readline().strip())

        solve(n, case_number)


if __name__ == "__main__":
    main()
