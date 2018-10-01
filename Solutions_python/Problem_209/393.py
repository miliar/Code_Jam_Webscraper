
import math

def solve(fin):
    parts = fin.readline().split()
    n = int(parts[0])
    k = int(parts[1])
    cs = []
    for i in xrange(n):
        parts = fin.readline().split()
        c = {"r": float(parts[0]), "h": float(parts[1]), "rh": float(parts[0])*float(parts[1])}
        cs.append(c)
    cs.sort(key = lambda x: x["r"])
    mx = 0.0
    for i in xrange(n):
        base = cs[i]["r"] * cs[i]["r"] + 2.0 * cs[i]["rh"]
        cl = []
        for j in xrange(n):
            if i != j and cs[j]["r"] <= cs[i]["r"]:
                cl.append(cs[j])
            if cs[j]["r"] > cs[i]["r"]:
                break
        if len(cl) < k-1:
            continue
        cl.sort(key = lambda x: x["rh"], reverse = True)
        for j in xrange(k-1):
            base += cl[j]["rh"] * 2.0
        if base > mx:
            mx = base
    return mx * math.pi


with open("a.in", "r") as fin:
    with open ("a.out", "w") as fout:
        t = int(fin.readline())
        for i in xrange(t):
            res = str(solve(fin))
            print i+1, res
            fout.write("Case #%d: %s\n" % (i+1, res))
