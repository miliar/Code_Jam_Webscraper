def solve():
    n, p = map(int, raw_input().split())
    r = map(int, raw_input().split())
    q = []
    for i in xrange(n):
        a = map(int, raw_input().split())
        a.sort()
        q.append(a)
    point = [0 for i in xrange(n)]
    for i in xrange(n):
        point[i] = 0
        for j in xrange(p):
            if q[i][j] * 100 < r[i] * 90:
                point[i] += 1
            else:
                break
    ans = 0
    low = [None for i in xrange(n)]	
    high = [None for i in xrange(n)]
    while True:
        check = False
        for i in xrange(n):
            if point[i] == p:
                check = True
        if check:
            break
        z = 0
        mn = 10**9
        mx = -1
        for i in xrange(n):
            low[i] = (100 * q[i][point[i]] + 110 * r[i] - 1) // (110 * r[i])
            high[i] = (100 * q[i][point[i]]) // (90 * r[i])
            if high[i] < high[z]:
                z = i
            mn = min(mn, high[i])
            mx = max(mx, low[i])
        if mn == 0 or mn < mx:
            point[z] += 1
        else:
            ans += 1
            for i in xrange(n):
                point[i] += 1
    return ans


def main():
    t = int(raw_input())
    for tst in xrange(t):
        ans = solve()
        print "Case #{0}: {1}".format(tst + 1, ans)

if __name__ == '__main__':
    main()
