from sortedcontainers import SortedDict

def solve():
    n, k = map(int, raw_input().split())
    cnts = SortedDict([(n, 1)])
    i = 0
    while i < k:
        sz, cnt = cnts.peekitem()
        ls = (sz-1) / 2
        rs = sz / 2
        if ls:
            cnts[ls] = cnts.get(ls, 0) + cnt
        if rs:
            cnts[rs] = cnts.get(rs, 0) + cnt
        del cnts[sz]
        i += cnt
    return "%d %d" % (rs, ls)

t = int(input())
for i in range(1, t+1):
    print("Case #%d: %s"%(i, solve()))
