#!/usr/bin/env python


T = int(raw_input())
for t in range(T):
    n, k = [int(s) for s in raw_input().split(" ")]
    u = float(raw_input())
    p = [float(s) for s in raw_input().split(" ")]
    ok = False
    p.sort()
    _u = u
    for i, (nwp, nxp) in enumerate(zip(p, p[1:])):
        if u > (nxp-nwp)*(i+1):
            u -= (nxp-nwp)*(i+1)
            continue
        else:
            nwp += u/(i+1)
            res = nwp**(i+1) * reduce(lambda x, y: x*y, p[i+1:])
            ok = True
            break

    if not ok:
        _p = (sum(p)+_u)/len(p)
        res = _p**len(p)
    print "Case #%d: %f" % (t+1, res)
            
