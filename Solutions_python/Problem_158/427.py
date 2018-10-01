#!/usr/bin/env python3

def solve(x, r, c): # r <= c
    if r*c%x != 0:
        return True
    if x == 1 or x == 2:
        return False
    if x == 3:
        return r == 1
    if x == 4:
        return r <= 2
    if x == 5:
        return r <= 2
    if x == 6:
        return r <= 3
    if x >= 7:
        return True

if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1):
        x, r, c = [int(x) for x in input().split()]
        r, c = min(r, c), max(r, c)
        print('Case #{0}:'.format(i),
                'RICHARD' if solve(x, r, c) else 'GABRIEL')
