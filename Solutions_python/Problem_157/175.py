mul = lambda a, b: ([[0,1,2,3],[1,0,3,2],[2,3,0,1],[3,2,1,0]][a[0]][b[0]],
                   (a[1]^b[1]^[[0]*4,[0,1,0,1],[0,1,1,0],[0,0,1,1]][a[0]][b[0]])%2)
def divide(s, x):
    if s is None: return None
    r = (0, 0)
    for i, c in enumerate(s):
        r = mul(r, c)
        if r == x: return s[i+1:]
for t in xrange(input()):
    l, x = map(int, raw_input().split())
    s = map(lambda a: ('1ijk'.index(a), 0), raw_input()) * min(12+x%4, x)
    s = reduce(divide, [(i+1, 0) for i in xrange(3)], s)
    print 'Case #%d: %s' % (t+1, 'NO' if s is None or reduce(mul, s, (0, 0)) != (0, 0) else 'YES')
