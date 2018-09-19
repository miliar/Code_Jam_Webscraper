#!/usr/bin/env python
import string
def read_tr():
    a = []
    a.append("ejp mysljylc kd kxveddknmc re jsicpdrysi")
    a.append("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd")
    a.append("de kr kd eoya kw aej tysr re ujdr lkgc jv")
    b = []
    b.append("our language is impossible to understand")
    b.append("there are twenty six factorial possibilities")
    b.append("so it is okay if you want to just give up")

    d = {}
    for j, s in enumerate(a):
        t = b[j]
        for i, c in enumerate(s):
            d[c] = t[i]

    d['q'] = 'z'
    d['z'] = 'q'
    
    return d

def main():
    T = int(raw_input())
    d = read_tr()

    for i in range(0, T):
        s = raw_input()
        t = s.translate(string.maketrans(''.join(d.keys()), ''.join(d.values())))
        print "Case #%d: %s" % ((i + 1), t)
    

if __name__ == '__main__':
    main()
