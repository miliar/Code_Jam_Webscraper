


def dfs(u): 
    if u in used: return 0
    used.add(u);
    return 1 + dfs(d[u])




T = int(raw_input());
d = None;
used = set();
for t in xrange(T):
    n = int(raw_input());
    s = map(int, raw_input().strip('\n').split());
    #print n, s

    d = {}
    used = set();
    for i in xrange(n):
        d[i] = s[i] - 1;

    res = 0;
    for i in xrange(n):
        if i not in used:
            dd =  dfs(i);
            if dd == 1: dd = 0
            res += dd

    print "Case #%d: %d" %(t + 1, res)
