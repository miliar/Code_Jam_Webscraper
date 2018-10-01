

import sys
sn = sys.stdin

googlerese = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""
english = """our language is impossible to understand
 there are twenty six factorial possibilities
 so it is okay if you want to just give up"""

g2e = {'y': 'a', 'e': 'o', 'q': 'z', 'z' : 'q'}
gwords = googlerese.split()
ewords = english.split()
for gw, ew in zip(gwords, ewords):
    for gl, el in zip(gw, ew):
        g2e[gl] = el


#print >> sys.stderr, "Have", len(g2e), "pairs"
#for letter in [chr(ord('a') + x) for x in range(26)]:
#    if letter not in g2e.keys():
#        print >> sys.stderr, "Except(g)", letter
#    if letter not in g2e.values():
#        print >> sys.stderr, "Except(e)", letter

T = int(sn.readline())
for tcase in range(T):
    line = sn.readline().strip()
    output = ""
    for letter in line:
        if letter in g2e.keys():
            output += g2e[letter]
        else:
            output += letter
    print "Case #%d:" % (tcase+1), output

