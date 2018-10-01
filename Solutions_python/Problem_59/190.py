def insert(d, s):
    dd = d
    ret = 0
    for t in s:
        if t not in dd:
            dd[t] = {}
            ret += 1
        dd = dd[t]
    return ret


#f = open("A.in", "r")
import sys
f = sys.stdin
T = int(f.readline())
for t in range(T):
    n, m = [int(s) for s in f.readline().strip().split(' ')]
    d = {}
    for nn in range(n):
        s = f.readline().strip().split('/')
        s.pop(0)
        insert(d, s)
    c = 0
    for mm in range(m):
        s = f.readline().strip().split('/')
        s.pop(0)
        c += insert(d, s)
    print "Case #%d: %d" % (t+1, c)
