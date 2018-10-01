#!/usr/bin/env python
from sys import stdin


def process():
    num = [int(c) for c in stdin.readline().rstrip()]

    nines = len(num)
    for i in reversed(range(1, len(num))):
        if num[i - 1] > num[i]:
            num[i - 1] -= 1
            nines = i

    for i in range(nines, len(num)):
        num[i] = 9

    return int(''.join([str(x) for x in num]))


def main():
    N = int(stdin.readline())
    for i in range(N):
        print("Case #{}: {}".format(i + 1, process()))

if __name__ == '__main__':
    main()


