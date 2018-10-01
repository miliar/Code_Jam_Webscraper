#!/usr/bin/env python3


def min_friends(audience):
    standing = 0
    friends = 0

    for level, count in enumerate(audience):
        missing = max(0, level - standing)
        friends += missing
        standing += count + missing

    return friends


if __name__ == '__main__':
    for i in range(int(input())):
        audience = input().split()[1]
        print('Case #{}: {}'.format(i + 1, min_friends(map(int, audience))))
