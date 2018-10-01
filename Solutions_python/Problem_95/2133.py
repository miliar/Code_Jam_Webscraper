from sys import stdin
def readln():
    return stdin.readline().rstrip()
def readlns(num):
    return map(str.rstrip,stdin.readlines(num))
ALPHA='abcdefghijklmnopqrstuvwxyz'

m = {'y':'a','e':'o','q':'z'}
for s in [('ejp mysljylc kd kxveddknmc re jsicpdrysi','our language is impossible to understand'),
          ('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd','there are twenty six factorial possibilities'),
          ('de kr kd eoya kw aej tysr re ujdr lkgc jv','so it is okay if you want to just give up')]:
    for x,y in zip(*s):
        if not x in ALPHA: continue
        if x in m:
            assert m[x] == y, "Inconsistency"
        else:
            m[x] = y

missing1 = [x for x in ALPHA if not x in m.keys()][0]
missing2 = [x for x in ALPHA if not x in m.values()][0]
m[missing1] = missing2
# Our mapping is complete, now read the input

def maplang(x):
    if x in ALPHA:
        return m[x]
    elif x.lower() in ALPHA: # Not sure if this is needed
        return m[x.lower()].upper()
    else:
        return x

N = int(readln())
for i,ln in enumerate(readlns(N)):
    print "Case #%d: %s" % (i+1, ''.join(map(maplang, ln)))
    