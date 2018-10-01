def solve():
    n, r, o, y, g, b, v = map(int, raw_input().split())
    plain = {'R': r, 'Y': y, 'B': b}
    cmplx = {'R': g, 'Y': v, 'B': o}
    clet = {'R': 'G', 'Y': 'V', 'B': 'O'}
    plet = {y: x for x, y in clet.items()}
    chars = plain.keys()
    res = []

    while sum(len(x) for x in res) < n:
        prev = res[-1][-1] if res else None
        if prev is None:
            for c in plain:
                if plain[c] != 0:
                    plain[c] -= 1
                    res.append(c)
                    break
        elif prev in plain.keys():
            if cmplx[prev] != 0:
                cmplx[prev] -= 1
                res.append(clet[prev])
            else:
                s = set("RYB")
                s.discard(prev)
                c = max(s, key = lambda x: plain[x])
                plain[c] -= 1
                res.append(c)
        else:
            let = plet[prev]
            res.append(let)
            plain[let] -= 1
    for v in plain.values():
        if v != 0:
            return "IMPOSSIBLE"
    for v in cmplx.values():
        if v != 0:
            return "IMPOSSIBLE"
    res = ''.join(res)
    for i in xrange(-1, len(res) - 1):
        if res[i] == res[i + 1]:
            return "IMPOSSIBLE"
    return res

t = int(raw_input())
for i in xrange(1, t + 1):
    print 'Case #{}: {}'.format(i, solve())
                  
        
