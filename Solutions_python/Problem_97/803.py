#from __future__ import division
import sys

rl = lambda: sys.stdin.readline().strip()

for c in range(int(rl())):
    A, B = map(int, rl().split())
    
    ans = 0
    for i in range(A,B+1):
        n = str(i)
        temp = []
        for j in range(len(n)):
            m = n[j+1:] + n[:j+1]
            if int(n)<int(m) and int(m)<=B:
                temp.append(m)
        ans += len(set(temp))
    print 'Case #%d: %d' % (c+1, ans)