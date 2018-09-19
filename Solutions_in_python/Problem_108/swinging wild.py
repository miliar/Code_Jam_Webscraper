from sys import stdin as I
from collections import deque

def solve(vv, D):
    v = [(0, 0)]
    v.extend(vv)
    #print v, len(v)
    
    r = v[0][0]
    m = v[0][0] + r
    i = 1
    n = len(v)
    if n > 1:
        dp = [n+1]*(n+1)
        work = deque()
        work.append((1, 0))
        dp[1] = 0
        while work:
            at = work[0]
            work.popleft()
            
            if at[1] != dp[at[0]]:
                continue
                
            r = min(v[at[0]][1], v[at[0]][0] - v[at[1]][0])
            x = v[at[0]][0] + r
            m = max(m, x)
            
            for j in xrange(at[0]+1, n):
                if v[j][0] <= x and dp[j] > at[0]:
                    work.append((j, at[0]))
                    dp[j] = at[0]
                    
    return "YES" if (m >= D) else "NO"
    
T = int(I.readline())
for C in xrange(1, T+1):
    n = int(I.readline())
    v = [[int(part) for part in I.readline().split()] for i in xrange(n)]
    D = int(I.readline())
    
    rv = solve(v, D)
    print "Case #%d: %s" % (C, rv)