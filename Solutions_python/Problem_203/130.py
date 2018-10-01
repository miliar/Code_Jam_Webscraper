import sys
from collections import defaultdict

def fillrow(row):
    first = None
    for r in row:
        if r != '?':
            first = r
            break
    if first is None:
        return None
    ans = []
    cur = first
    for r in row:
        if r != '?':
            cur = r
        ans.append(cur)
    return ans

def run(R, C, g):
    ans = []
    for row in g:
        ans.append(fillrow(row))
    moo = None
    for row in ans:
        if row is not None:
            moo = row
            break
    ans2 = []
    for row in ans:
        if row is not None:
            moo = row
        ans2.append(moo)
    return ans2


f = file(sys.argv[1],'r')
T = int(f.readline().strip())
for case in range(1,T+1):
    R,C = f.readline().strip().split()
    grid = [list(f.readline().strip()) for r in range(int(R))]
    ans = run(int(R), int(C), grid)
    print 'Case #%d:' % (case,)
    for a in ans:
        print ''.join(a)
