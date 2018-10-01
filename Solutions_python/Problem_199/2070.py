

def flip(s, st, k):
    for ki in xrange(k):
        s[st + ki] = abs(1 - s[st + ki])


t = int(raw_input())

for ti in xrange(1, t + 1):
    sraw, k = raw_input().split(" ")
    k = int(k)
    s = [0] * len(sraw)
    isok = True
    for i, si in enumerate(sraw):
        s[i] = 1 if si == "+" else 0
        if not s[i]:
            isok = False

    if isok:
        print "Case #{}: {}".format(ti, 0)
        continue

    num = 0
    for st in xrange(0, len(s) - k + 1):
        if s[st] == 0:
            flip(s, st, k)
            num += 1

    if sum(s) < len(s):
        print "Case #{}: {}".format(ti, "IMPOSSIBLE")
    else:
        print "Case #{}: {}".format(ti, num)
