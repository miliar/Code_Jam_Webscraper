import sys

T = sys.stdin.readline()
t = sys.stdin.readlines()
N = 10
groups = [t[n:n + N] for n in range(0, len(t), N)]
for i, z in enumerate(groups):
    y_fa = int(z.pop(0))
    y_sa = int(z.pop(4))
    z_fa = y_fa - 1
    z_sa = y_sa - 1

    a1 = z[0:4]
    a2 = z[4:8]
    k1 = [x.split() for x in a1]
    k2 = [x.split() for x in a2]
    j1 = [map(int, x) for x in k1]
    j2 = [map(int, x) for x in k2]

    derp = []
    derp.append(j1[vars()['z_fa']])
    derp.append(j2[vars()['z_sa']])

    g = list(set.intersection(*map(set, derp)))

    if len(g) == 1:
        print 'Case #%d: %d' % (i + 1, g[0])
    elif len(g) > 1:
        print 'Case #%d: Bad Magician!' % (i + 1)
    elif len(g) == 0:
        print 'Case #%d: Volunteer Cheated!' % (i + 1)
