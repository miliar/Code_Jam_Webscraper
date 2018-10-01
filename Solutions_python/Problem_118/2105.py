import math
import sys


def read_cases(f):
    f.readline()
    tmp = read_case(f)
    while tmp:
        yield tmp
        tmp = read_case(f)


def read_case(f):
    params = f.readline()
    if not params:
        return None
    return [int(x) for x in params.strip().split()]


def palindrome(x):
    strx = str(x)
    for i in range(len(strx) / 2 + 1):
        if strx[i] != strx[len(strx) - i - 1]:
            return False
    return True


def square(n):
    if n == 1:
        return True
    x = n / 2
    seen = {x}
    while x * x != n:
        x = (x + (n / x)) / 2
        if x in seen:
            return False
        seen.add(x)
    return True


def num_fair_squares(lo, hi):
    total = 0
    for n in range(lo, hi + 1):
        if square(n) and palindrome(n):
            if palindrome(int(math.sqrt(n) + 0.5)):
                total += 1
    return total


def main(argv):
    with open(argv[1]) as f:
        for n, case in enumerate(read_cases(f)):
            print "Case #%d: %d" %(n + 1, num_fair_squares(*case))


if __name__ == "__main__":
    main(sys.argv)
