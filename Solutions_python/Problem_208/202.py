t = int(input())
def dfs(e, s, es, ds, j, v):
    t1 = t2 = None
    if j == v-1:
        return 0
    d = ds[j][j+1]
    if es[j][0] >= d:
        t1 = d/es[j][1] + dfs(es[j][0] - d, es[j][1], es, ds, j+1, v)
    if e >= d:
        t2 = d/s + dfs(e - d, s, es, ds, j+1, v)
    if t1 is None and t2 is None:
        return None
    if t1 is None:
        return t2
    if t2 is None:
        return t1
    return min(t1,t2)

for i in range(t):
    n, q = [int(x) for x in input().split(" ")]
    es = []
    ds =[]
    for j in range(n):
        e, s = [int(x) for x in input().split(" ")]
        es.append((e,s))
    for j in range(n):
        ds.append([int(x) for x in input().split(" ")])
    for j in range(q):
        u, v = [int(x) for x in input().split(" ")]
    # small
    t = dfs(0, 0, es, ds, 0, v)
    #ce = 0
    #cs = 0
    #t = 0
    #for j in range(v-1):
    #    d = ds[j][j+1]
    #    if es[j][0] >= d and (es[j][1] >= cs or ce < d):
    #        ce = es[j][0] - d
    #        cs = es[j][1]
    #    else:
    #        ce -= d
    #    t += d/cs 

    print("Case #" + str(i+1) + ": "+str(t))
