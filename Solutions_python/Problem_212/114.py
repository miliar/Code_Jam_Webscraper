import sys
sys.setrecursionlimit(1000000)


# sys.stdin = open('a1.in')
# sys.stdin = open('A-small-attempt0.in')
sys.stdin = open('A-large.in')
sys.stdout = open('out.txt', 'w')


def read_int():
    return int(input())


def read_int_list():
    return list(map(int, input().split()))


h = {}


def f(p, c, s):
    if (c, s) in h:
        return h[(c, s)]
    if sum(c) == 0:
        res = 0
        h[(c,s)] = res
        return res
    res = 0
    cc = list(c)
    for i in range(p):
        if cc[i] == 0:
            continue
        cc[i] -= 1
        r = int(s == 0) + f(p, tuple(cc), (s + i) % p)
        if r > res:
            res = r
        cc[i] += 1
    h[(c, s)] = res
    return res


def solve_it():
    global h
    n, p = read_int_list()
    g = read_int_list()
    c = [0] * p
    for gg in g:
        c[gg % p] += 1
    res = c[0]
    c[0] = 0
    h = {}
    res += f(p, tuple(c), 0)
    return res


def main():
    n_cases = int(input())
    for test_case in range(1, n_cases + 1):
        print(test_case, file=sys.stderr, end=' ')
        res = solve_it()
        print('Case #' + str(test_case) + ':', res)

    print(file=sys.stderr)


if __name__ == '__main__':
    main()
