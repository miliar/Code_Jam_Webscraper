#!/usr/bin/python3

import math

def is_fair(n):
    s = str(n)
    m = math.ceil(len(s) / 2)

    lower_half = s[:m]
    upper_half = s[-1:-m-1:-1]

    return lower_half == upper_half

def is_square_of_fair(n):
    sqrt = math.sqrt(n)
    i = int(sqrt)

    if i != sqrt:
        # not a square
        return False

    return is_fair(i)

def test_interval(A, B):
    hits = 0

    for i in range(A, B+1):
        if is_fair(i) and is_square_of_fair(i):
            hits += 1

    return hits

def main():
    no_test_cases = int(input())

    for i in range(1, no_test_cases + 1):
        A, B = map(int, input().split())
        result = test_interval(A, B)

        print('Case #{0}: {1}'.format(i, result))

if __name__ == '__main__':
    main()
