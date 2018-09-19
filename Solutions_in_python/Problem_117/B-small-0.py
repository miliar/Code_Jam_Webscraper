import sys

sys.stdin = open('B-small-0.in', 'r')
sys.stdout = open('B-small-0.out', 'w')

T = int(input())


def solution():
    N,M = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(N)]
    ar = [[a[i][j] for i in range(N)] for j in range(M)]

    for i in range(N):
        for j in range(M):
            if a[i][j] == 1:
                if (a[i] != [1] * M) and (ar[j] != [1] * N):
                    return "NO"
    return "YES"

for test in range(T):
    test += 1
    print("Case #%03d:" % test, end = ' ', file = sys.stderr)
    print("Case #%d: %s" % (test, solution()))
    print("OK", file = sys.stderr)

