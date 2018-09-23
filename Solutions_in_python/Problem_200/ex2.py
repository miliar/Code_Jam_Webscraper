#!/usr/bin/env python3


def is_tidy(n):
    s = str(n)
    last = -1
    for d in s:
        d = int(d)
        if d < last:
            return False
        last = d
    return True


def get_biggest_tidy(upper_bound):
    for i in range(upper_bound, 0, -1):
        if is_tidy(i):
            return i
    return -1


def main():
    nb = int(input())
    numbers = []
    for _ in range(nb):
        numbers.append(int(input()))

    for (i, n) in enumerate(numbers):
        print("Case #{}: {}".format(i+1, get_biggest_tidy(n)))


if __name__ == '__main__':
    main()
