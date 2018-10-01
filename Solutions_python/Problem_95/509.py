#!/usr/bin/python
import sys

m = {}

a = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'
b = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'

i = 0
for c in b:
    m[c] = a[i]
    i = i + 1

m['q'] = 'z'
m['z'] = 'q'

n = int(sys.stdin.readline())
for i in xrange(n):
    s = sys.stdin.readline()
    t = ''
    for c in s:
        if c == ' ' or c == '\n':
            t += c
        else:
            t += m[c]
    sys.stdout.write('Case #%d: %s' % (i + 1, t))

