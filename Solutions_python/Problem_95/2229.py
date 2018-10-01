gg = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv"
en = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up"

trans = {'a':'y', 'o':'e', 'z':'q', 'q':'z'}

for a in range(len(gg)):
    trans[gg[a]] = en[a]

f = open ("A-small-attempt0.in", "r")
l = f.readlines ()
n = int(l[0])
l.pop (0)

for b in range(n):
    s = ""
    for x in l[b].strip ():
        s += trans[x]
    print "Case #%s: " % (b+1) + s
