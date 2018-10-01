sam = (('ejp mysljylc kd kxveddknmc re jsicpdrysi', 'our language is impossible to understand'),
       ('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'there are twenty six factorial possibilities'),
       ('de kr kd eoya kw aej tysr re ujdr lkgc jv', 'so it is okay if you want to just give up'))

dic1 = {}
[dic1.update(zip(s[0],s[1])) for s in sam]
dic2 = dic1.copy()
dic1['q'] = 'q'
dic1['z'] = 'z'
dic2['q'] = 'z'
dic2['z'] = 'q'

deals = [(dic1,r'c:\a1.out'), (dic2, r'c:\a2.out')]
for (dic, fn) in deals:
    f = open(r'c:\A-small-attempt3.in')
    of = open(fn, 'w')
    f.readline()
    l = f.readline().strip()
    i = 1
    while l:
        o = ''.join([dic[L] for L in l])
        print('Case #%d: %s'%(i,o), file=of)
        i+=1
        l = f.readline().strip()

    f.close()
    of.close()