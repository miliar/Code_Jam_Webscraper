import cPickle as pickle


def calc(n, m, k):
    if n == 5 and m == 5 and n * m - k < 4 and n * m != k:
        return 'Impossible'
    a = [[0 for i in range(m)] for j in range(n)]

    def add(c, i, j, delta=1):
        cnt = 0
        for x in (i - 1, i, i + 1):
            for y in (j - 1, j, j + 1):
                if x < 0 or y < 0 or x >= n or y >= m or x == i and y == j:
                    continue
                if a[x][y] == 0:
                    c[x][y] += delta
        c[i][j] = -1

    def ok(a):
        c = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if a[i][j]:
                    add(c, i, j)

        sx, sy = None, None
        for i in range(n):
            for j in range(m):
                if c[i][j] == 0:
                    sx, sy = i, j

        b = [[False for i in range(m)] for j in range(n)]

        def flood_fill(x, y):
            b[x][y] = True
            for i in (x - 1, x, x + 1):
                for j in (y - 1, y, y + 1):
                    if (i >= 0 and j >= 0 and i < n and j < m and
                            not b[i][j]):
                        b[i][j] = True
                        if c[i][j] == 0:
                            flood_fill(i, j)

        if sx is None:
            return False, sx, sy
        flood_fill(sx, sy)

        # print '\n'.join(map(str, a))
        # print '-' * 30
        # print '\n'.join(map(str, c))
        # print '-' * 30
        # print '\n'.join(map(str, b))
        # print '=' * 70

        for i in range(n):
            for j in range(m):
                if a[i][j] == 0 and not b[i][j]:
                    return False, sx, sy

        return True, sx, sy

    def dfs(dep, left):
        if left == 0:
            return ok(a)
        if dep >= n * m:
            return False, None, None

        i = dep / m
        j = dep % m
        for x in (0, 1):
            if x <= left:
                a[i][j] = x
                is_ok, sx, sy = dfs(dep + 1, left - x)
                if is_ok:
                    return is_ok, sx, sy
                a[i][j] = 0
        return False, None, None

    ans = 'Impossible'
    is_ok, sx, sy = dfs(0, k)
    if is_ok:
        ans = ''
        for i in range(n):
            for j in range(m):
                if i == sx and j == sy:
                    ans += 'c'
                elif a[i][j] == 0:
                    ans += '.'
                else:
                    ans += '*'
            ans += '\n'
    return ans


def main():
    # print calc(2, 3, 1)
    d = {}
    for n in range(1, 6):
        for m in range(1, 6):
            for k in range(0, n * m + 1):
                print n, m, k
                ans = calc(n, m, k)
                d['%s-%s-%s' % (n, m, k)] = ans

    f = open('c.pickle', 'wb')
    pickle.dump(d, f)
    f.close()


if __name__ == "__main__":
    main()
