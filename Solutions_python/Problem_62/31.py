#!/usr/bin/env python
p = 'A'
s = 'small-attempt%d' % 0
l = 'large'
current = '%s-%s' % (p, l)

f = open('%s.in' % current, 'r')
g = open('%s.out' % current, 'w')
lines = f.readlines()
f.close()

t = int(lines[0])

line = 1
for i in xrange(1, t + 1):
    n = int(lines[line])
    line += 1
    wires = []
    count = 0
    for j in xrange(n):
        row = lines[line + j].split()
        a, b = map(int, row)
        for k in wires:
            if (a - k[0]) * (b - k[1]) < 0:
                count += 1
        wires.append((a, b))
    line += n
    print "Case #%d: %d" % (i, count)
    g.write("Case #%d: %d\n" % (i, count))

g.close()
