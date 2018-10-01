import sys
assert sys.version_info >= (3, 5)
from math import ceil, floor
from itertools import permutations
#from fractions import Fraction
Fraction = int


def nonempty(t0, t1):
    if t0[1] < t1[0] or t1[1] < t0[0]:
        return False
    if t0[0] <= t0[1] and t1[0] <= t1[1]:
        return True
    return False


def solve(prefix):
    N, P = [int(_) for _ in input().split()]
    R = [int(_) for _ in input().split()]
    Q = []
    print(prefix, file=sys.stderr)
    for i in range(N):
        Qi = [int(_) for _ in input().split()]
        Qi.sort(reverse=True)
        Q.append([(ceil(Fraction(int(_)*10)/Fraction(R[i]*11)), floor(Fraction(int(_)*10)/Fraction(R[i]*9))) for _ in Qi])
        print(Q[i], file=sys.stderr)
    ans = 0
    while True:
        mi = None
        midx = None
        term = False
        for i in range(N):
            if len(Q[i]) == 0:
                term = True
                break
            if mi is None or Q[i][-1] < mi:
                mi = Q[i][-1]
                midx = i
        if term:
            break
        cnt = 0
        for i in range(N):
            if nonempty(mi, Q[i][-1]):
                cnt += 1
        if cnt < N:
            Q[midx].pop()
            continue
        ans += 1
        for i in range(N):
            Q[i].pop()
    print('{}{}'.format(prefix, ans))


def main():
    T = int(input())
    for t in range(T):
        solve(prefix='Case #{}: '.format(t+1))


if __name__ == '__main__':
    main()
