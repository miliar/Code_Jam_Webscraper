import sys
from itertools import combinations

rl = lambda: sys.stdin.readline().strip()


ds = 0
cache = {}
min_ans = 987654321


def foo(stack, remain, nd):
    global ds
    global min_ans
    global cache
    k = str((stack, remain))
    #print k, k in cache
    if k in cache:
        v = cache[k]
        if v < nd:
            return v
    cache[k] = nd
    if not remain:
        min_ans = min(min_ans, nd)
        #print stack, remain, nd
    print stack, remain, nd
    for f in remain:
        r = remain[::]
        r.remove(f)
        foo(stack + [f], r, nd + 1)
    for f in combinations(remain, 2):
        if f[0][1] + f[1][1] <= ds:
            r = remain[::]
            r.remove(f[0])
            r.remove(f[1])
            foo(sorted(stack + [f[0], f[1]]), sorted(r), nd + 1)


T = int(rl())

for tcase in range(T):
    n, ds = map(int, rl().split())
    files = map(int, rl().split())
    min_ans = 987654321

    print >> sys.stderr, tcase
    files.sort()
    ans = 0
    while files:
        f = files[-1]
        ans += 1
        files.pop()
        found = False
        for i in range(len(files)):
            if files[i] + f <= ds:
                found = i
                break
        if found is not False:
            files = [f for idx, f in enumerate(files) if idx != found]
    print 'Case #%d: %d' % (tcase + 1, ans)
