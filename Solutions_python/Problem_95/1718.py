#!/usr/bin/python

import sys

coded = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'
plain = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'

code = dict(zip(coded, plain))
# hints in problem
code['q'] = 'z'
code['e'] = 'o'
code['y'] = 'a'
# follows from bijectivity
code['z'] = 'q'

def decode(x, code=code):
    return ''.join([code[c] for c in x])

n = int(sys.stdin.readline().strip())
for i in range(1, n+1):
    print "Case #%d: %s" % (i, decode(sys.stdin.readline().strip()))
