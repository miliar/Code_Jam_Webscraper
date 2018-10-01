import sys
from collections import defaultdict

# sys.stdin = open('a1.in')
# sys.stdin = open('A-small-attempt0.in')
sys.stdin = open('A-large.in')
sys.stdout = open('out.txt', 'w')


def solve_it(r, c, a):
    for i in range(r):
        ok = True
        for j in range(c):
            ok &= a[i][j] == '?'
        if not ok:
            l = '?'
            for j in range(c):
                if a[i][j] != '?':
                    l = a[i][j]
                a[i][j] = l
            l = '?'
            for j in range(c-1, -1, -1):
                if a[i][j] != '?':
                    l = a[i][j]
                a[i][j] = l
    for j in range(c):
        l = '?'
        for i in range(r):
            if a[i][j] != '?':
                l = a[i][j]
            a[i][j] = l
        l = '?'
        for i in range(r-1, -1, -1):
            if a[i][j] != '?':
                l = a[i][j]
            a[i][j] = l
    res = '\n' + '\n'.join([''.join(row) for row in a])
    return res


def main():
    n_cases = int(input())
    for test_case in range(1, n_cases + 1):
        r, c = map(int, input().split())
        a = [list(input()) for _ in range(r)]
        print(test_case, file=sys.stderr, end=' ')
        res = solve_it(r, c, a)
        print('Case #' + str(test_case) + ':', res)

    print(file=sys.stderr)


if __name__ == '__main__':
    main()
