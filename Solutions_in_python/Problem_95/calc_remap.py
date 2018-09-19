#!/usr/bin/python

import sys;

s1 = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv zq'
s2 = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up qz'

remap = dict();
backRemap = dict();

for (c1, c2) in zip(s1, s2):
    c3 = remap.get(c1);
    if c3 and c3 != c2:
        print "error: ", c1, c2, c3;
    c3 = backRemap.get(c2);
    if c3 and c3 != c1:
        print "error1: ", c1, c2, c3;
    remap[c1] = c2;
    backRemap[c2] = c1;

backRemap[' '] = ' ';
#print remap;

#print len(remap), len(backRemap)

nt = int(sys.stdin.readline().strip());

def translate(s):
    res = '';
    for c in s:
        res += remap[c];
    return res;

for t in range(1, nt + 1):
    print "Case #%d: %s" % (t, translate(sys.stdin.readline().strip()));
