def calc(n, ss, d):
    dp = {}
    dp[ss[0][0]] = ss[0][0]
    for j in xrange(d + 1):
        if j in dp:
            for k in ss:
                if j < k[0] and j + dp[j] >= k[0]:
                    #print k[0]
                    if k[0] in dp:
                        dp[k[0]] = max(dp[k[0]], min(k[0] - j, k[1]))
                    else:
                        dp[k[0]] = min(k[0] - j, k[1])
                    if k[0] == d:
                        return True
    return False



t = int(raw_input())
i = 1
while i <= t:
    n  = int(raw_input())
    ss = [[0, 0]] * n
    for j in xrange(n):
        ss[j] = [int(x) for x in raw_input().split(' ')]
    d  = int(raw_input())
    
    ss.append([d, 0])
    
    #print n
    #print ss
    #print d
    
    res = "YES" if calc(n, ss, d) else "NO"
    
    print "Case #%s: %s" % (i, res)
    
    i += 1
