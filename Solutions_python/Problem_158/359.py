#!/usr/bin/python2

R = 'RICHARD'
G = 'GABRIEL'

table = {(3, 1, 3): R,
         (3, 2, 3): G,
         (3, 3, 3): G,
         (3, 3, 4): G,
         (4, 2, 2): R,
         (4, 1, 4): R,
         (4, 2, 4): R,
         (4, 3, 4): G,
         (4, 4, 4): G}

def main():
    n = input()
    for t in range(n):
        li = map(int, raw_input().split())
        print 'Case #{}: {}'.format(t + 1, solve(*li))

def solve(x, r, c):
    key = [x] + sorted([r, c])
    if x == 1:
        return G
    elif x == 2:
        if r * c % 2 != 0:
            return R
        return G
    elif x == 3 and r * c % 3 != 0:
        return R
    elif x == 4 and r * c % 4 != 0:
        return R
    else:
        return table[tuple(key)]

main()
