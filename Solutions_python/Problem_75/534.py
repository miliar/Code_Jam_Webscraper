inf = open("b.in", "r")
ouf = open("b.out", "w")
T = int(inf.readline())
for t in range(T):
    print >> ouf, "Case #" + str(t + 1) + ":",
    parts = inf.readline().split()
    n = int(parts[0])
    pos = 1
    comb = {}
    for i in xrange(pos, pos + n):
        x = parts[i][0]
        y = parts[i][1]
        z = parts[i][2]
        comb[x + y] = z
        comb[y + x] = z
    pos += n

    n = int(parts[pos])
    pos += 1
    opp = {}
    for i in xrange(ord('A'), ord('Z')):
        opp[chr(i)] = []
    for i in xrange(pos, pos + n):
        x = parts[i][0]
        y = parts[i][1]
        opp[x] += y
        opp[y] += x
    pos += n

    n = int(parts[pos])
    s = parts[pos + 1]
    l = [s[0]]
    for i in xrange(1, n):
        last = ''
        if len(l) > 0:
            last = l[-1]
        pair = last + s[i]
        if pair in comb:
            l.pop()
            l += comb[pair]
        else:
            for c in opp[s[i]]:
                if l.count(c) != 0:
                    l = []
                    break
            else:
                l += s[i]
    s = '{0}'.format(l)
    res = ''
    for c in filter(lambda c: c != '\'', s):
        res += c
    print >> ouf, res
inf.close()
ouf.close()
