# -*- coding: utf-8 -*-
T = int(raw_input())

for case in xrange(1, T + 1):
    N, P = map(int, raw_input().split())
    G = map(int, raw_input().split())
    a = [0]*4
    dp = [[[0]*105 for i in xrange(105)] for i in xrange(105)]
    for Gi in G:
        a[Gi%P] += 1

    for i in xrange(105):
        if i > a[1]: continue
        for j in xrange(105):
            if j > a[2]: continue
            for k in xrange(105):
                if k > a[3]: continue
                if i > 0:
                    d = 1 if ((i - 1) + 2*j + 3*k)%P == 0 else 0
                    dp[i][j][k] = max(dp[i - 1][j][k] + d, dp[i][j][k])
                if j > 0:
                    d = 1 if (i + 2*(j - 1) + 3*k)%P == 0 else 0
                    dp[i][j][k] = max(dp[i][j - 1][k] + d, dp[i][j][k])
                if k > 0:
                    d = 1 if (i + 2*j + 3*(k - 1))%P == 0 else 0
                    dp[i][j][k] = max(dp[i][j][k - 1] + d, dp[i][j][k])
    ans = dp[a[1]][a[2]][a[3]] + a[0]
    print "Case #%d: %d" % (case, ans)

