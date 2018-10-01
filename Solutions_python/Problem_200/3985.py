import sys


def last_tidy(n):
    n_list = [int(c) for c in n]

    ok = False

    while not ok:
        ok = True
        for i in range(len(n_list) - 1):
            if n_list[i] > n_list[i + 1]:
                n_list[i] -= 1
                for j in range(i + 1, len(n_list)):
                    n_list[j] = 9
                ok = False
                break

    if n_list[0] == 0:
        del n_list[0]

    return ''.join(str(d) for d in n_list)


def solve():
    t = int(sys.stdin.readline().strip())

    for i in xrange(t):
        n = sys.stdin.readline().strip()
        print 'Case #{}: {}'.format(i + 1, last_tidy(n))


if __name__ == '__main__':
    solve()
