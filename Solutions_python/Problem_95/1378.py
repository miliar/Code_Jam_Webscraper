import sys
f = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvqz1234567890"
o = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upzq1234567892"

mapping = {}

for a, b in zip(f, o):
    mapping[a] = b

for c, line in enumerate(sys.stdin):
    print "Case #%d:" % (c, ),
    print ''.join(map(lambda x: mapping[x], line.rstrip()))
