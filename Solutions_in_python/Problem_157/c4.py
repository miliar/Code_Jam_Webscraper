import math
import sys
import collections
import functools

#fin = sys.arg[1]
fin = "./C-small-attempt5.in"
#fin = "./c.in"
#fin = "./c_joao.in"

with open(fin) as f:
    lines = f.readlines()

def tab(a,b):
    mult = ""
    if a.startswith("-") and b.startswith("-"):
        mult = ""
    elif a.startswith("-") or b.startswith("-"):
        mult = "-"
    if a.startswith("-"):
        a = a[1:]
    if b.startswith("-"):
        b = b[1:]

    if a == '1':
        return mult + b
    if b == '1':
        return mult + a

    if a == 'i' and b == 'i':
        if mult == '-':
            return '1'
        return '-1'
    if a == 'i' and b == 'j':
        return mult + 'k'
    if a == 'i' and b == 'k':
        if mult == '-':
            return 'j'
        return '-j'

    if a == 'j' and b == 'i':
        if mult == '-':
            return 'k'
        return '-k'
    if a == 'j' and b == 'j':
        if mult == '-':
            return '1'
        return '-1'
    if a == 'j' and b == 'k':
        return mult + 'i'

    if a == 'k' and b == 'i':
        return mult + 'j'
    if a == 'k' and b == 'j':
        if mult == '-':
            return 'i'
        return '-i'
    if a == 'k' and b == 'k':
        if mult == '-':
            return '1'
        return '-1'

for case, ln in enumerate(range(1, len(lines), 2)):

    a, b = map(int, lines[ln].split())
    s = lines[ln+1].strip()

    s = s*b
    ans = False

    while True:
        sb = len(s)
        for a in ["iiii", "jjjj", "kkkk"]:
            s = s.replace(a,"")
        if len(s) == sb:
            break


    if len(s) < 3 or len(set(s) ) <= 1:
        print "Case #%d: NO" % (case + 1)
        continue

    qti = 0

    def go(s):
        p = s[0]
        for i in range(1, len(s)):
            p = tab(p, s[i])
        return p

    ri = go(s)

    if ri != '-1':
        print "Case #%d: NO" % (case + 1)
        continue

    #--------------------------------------
    def back(s):
        p = s[-1]
        for i in range(len(s)-2, -1, -1):
            p = tab(p, s[i])
        return p
    rk = back(s[::-1])

    #--------------------------------------
    if rk != '-1':
        print "Case #%d: NO" % (case + 1)
        continue


    ipos = []
    p = s[0]
    for i in range(1, len(s)-1):
        if p == "i":
            ipos.append(i)
        p = tab(p, s[i])

    if len(ipos) == 0:
        print "Case #%d: NO" % (case + 1)
        continue

    kpos = []
    p = s[len(s)-1]
    if p == "k":
        kpos.append(i)
    for i in range(len(s)-2, 1, -1):
        if p == "k":
            kpos.append(i)
        p = tab(s[i], p)
    kpos.reverse()

    if len(kpos) == 0:
        print "Case #%d: NO" % (case + 1)
        continue

    for i in ipos:
        p = s[i]
        #print "trying first till", kpos[0]
        #print "p", p
        j = 0
        for j in range(i+1,kpos[0]+1):
            #print "adding", s[j]
            p = tab(p, s[j])
            #print "results",p

        if p == 'j':
            ans = True
            break

        for next_ in kpos[1:]:
            #print "trying now till", next_
            for k in range(j, next_):
                p = tab(p, s[k])

            if p == 'j':
                ans = True
                break

    print "Case #%d: YES" % (case + 1)

    #print "s", s, "ri", ri, "rk",rk

