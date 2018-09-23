import math

def solve():
    n, q = map(int, input().split())
    h = [tuple(map(int, input().split())) for _ in range(n)]
    d = [list(map(int, input().split())) for _ in range(n)]
    u, v = map(int, input().split())
    assert u == 1
    assert v == n
    result = [0] * n
    for i in range(n - 2, -1, -1):
        m = float('inf')
        dis = 0
        for j in range(i + 1, n):
            assert d[j - 1][j] != 0
            dis += d[j - 1][j]
            if dis > h[i][0]:
                break
            m = min(m, dis / h[i][1] + result[j])

        #print('result[%d]=%f' % (i, m))
        assert not math.isinf(m)
        result[i] = m
    print(result[0])

t = int(input())
for i in range(t):
    print('Case #%d: ' % (i + 1), end='')
    solve()