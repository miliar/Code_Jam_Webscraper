s1 = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'
s2 = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'

d = {}

for i in range(len(s1)):
    d[s1[i]] = s2[i]

d['z'] = 'q'
d['q'] = 'z'

N = input()
for i in range(N):
    ret = ''
    s = raw_input()
    for c in s:
        ret += d[c]
    print 'Case #%s: %s' % (i+1, ret)