
def ok(r, t, x):
    s = 0
    for i in range(1, x+1):
        s += ((i*2+r-1)**2 - (i*2+r-2)**2)
        if s > t:
            return False
    return True

"""
def ber(n):
    a = {}
    for i in range(n+1):
        a[i] = 1.0/(i+1)
        for j in range(i, 0, -1):
            a[j-1] = j*(a[j-1]-a[j])
    return a[0]
"""

def solve(r, t):
    i = 1
    while ok(r, t, i):
        i += 1
    return i - 1

T = input()
for i in xrange(1, T+1):
    r, t = map(int, raw_input().split())
    ret = solve(r, t)
    print 'Case #%d: %d' % (i, ret)

