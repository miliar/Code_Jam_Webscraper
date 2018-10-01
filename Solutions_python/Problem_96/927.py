import sys

T = sys.stdin.readline()
i = 0
for l in sys.stdin:
    count = 0
    i += 1
    data = map(int, l.split())
    N, S, p = data[0:3]
    G = data[3:]
    G.sort(key=lambda x: -x)
    for g in G:
        g -= p
        if g < 0:
            break
        if g >= (p - 1) * 2:
            count += 1
        elif g >= (p - 2) * 2 and S > 0:
            count += 1
            S -= 1
        else:
            break
    print "Case #{0}: {1}".format(i, count)

