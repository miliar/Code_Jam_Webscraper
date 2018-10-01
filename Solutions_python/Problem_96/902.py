
def genTriplet(i):
    t = []
    s = None
    if i % 3 == 0:
        t = [i/3]*3
        if i > 0:
            s = [i/3-1, i/3, i/3+1]
    elif i % 3 == 1:
        t = [i/3, i/3, i/3+1]
    else:
        t = [i/3, i/3+1, i/3+1]
        s = [i/3, i/3+2, i/3+2]
    return t, s


cases = int(raw_input())

for case in xrange(cases):
    casein = [int(x) for x in raw_input().split()]
    N = casein[0]
    S = casein[1]
    p = casein[2]
    total = 0
    for i in casein[3:]:
        t, s = genTriplet(i)
        if t[2] >= p:
            total += 1
        elif s:
            if s[2] >= p and t[2] < p and S > 0:
                total += 1
                S -= 1
    print "Case #%d: %d" % (case+1, total)
