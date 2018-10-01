
def test_usual(s, p):
    return (p == 0) or \
           ((p >= 1) and (p + 2*(p-1) <= s))
    
def test_surprising(s, p):
    if p < 2:
        return test_surprising(s, 2)
    else:
        return (s >= 2) and (p + 2*(p-2) <= s)

cases = int(raw_input())
for case in range(cases):
    comps = map(int, raw_input().strip().split())
    N, S, p, t = comps[0], comps[1], comps[2], comps[3:]
    v00 = v01 = v10 = v11 = 0
    for i in range(N):
        tu = test_usual(t[i], p)
        ts = test_surprising(t[i], p)
        result = 0
        if tu and ts:
            v11 = v11 + 1
        elif tu and not ts:
            v10 = v10 + 1
        elif not tu and ts:
            v01 = v01 + 1
        else:
            v00 = v00 + 1
        result = min(S, v01) + v10 + v11
    print 'Case #%d: %d' % (case + 1, result)

    