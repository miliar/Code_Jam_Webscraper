import os

def solve(s):
    m = 0
    for i in xrange(len(s)):
        if int(s[i]) < m:
            g = int(s)
            d = int(s[i:])+1
            return solve(str(g-d))
        m = max(m, int(s[i]))
    return s



with open(os.path.expanduser("~/PycharmProjects/gcj/2017/qualify/B.in")) as f:
    m = int(f.readline().strip('\n'))
    # print m
    for i in range(m):
        s = f.readline().strip()
        res = solve(s)
        print 'Case #' + str(i+1) + ': ' + str(res)