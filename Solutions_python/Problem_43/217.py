#!/usr/bin/python

t = raw_input()

for i in range(0, int(t)):
    string = raw_input()
    f = 100 * [0]
    w = "0123456789abcdefghijklmnopqrst"
    d = {}
    r = ''
    for s in string:
        if r == '':
            r += '1'
            d[s] = '1'
            f[1] = 1
            continue
        if d.has_key(s):
            r += d[s]
            continue
        for j in range(len(w)):
            if f[j] == 0:
                r += w[j]
                d[s] = w[j]
                f[j] = 1
                break
    #print r
    b = len(d)
    if b < 2:
        b = 2
    res = int(r, b)
    print 'Case #'+str(i+1)+': '+str(res)
