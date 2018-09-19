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
    s = lines[line].split()
    m, n = map(int, s)
    line += 1
    a = ['/']
    for j in xrange(m):
        row = lines[line + j]
        if row[-1:] == '\n':
            row = row[:-1]
        while row:
            if not row in a:
                a.append(row)
            row = row[:row.rindex('/')]
    line += m
    count = 0
    for j in xrange(n):
        row = lines[line + j]
        if row[-1:] == '\n':
            row = row[:-1]
        while row and not row in a:
            count += 1
            a.append(row)
            row = row[:row.rindex('/')]
    line += n
    print "Case #%d: %d" % (i, count)
    g.write("Case #%d: %d\n" % (i, count))

g.close()
