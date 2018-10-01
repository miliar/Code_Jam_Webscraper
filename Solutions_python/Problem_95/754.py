#!/usr/bin/env python

PAIRS = [("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand"),
         ("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities"),
         ("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up")]

mapping = {}
for i in "abcdefghijklmnopqrstuvwxyz":
    for enc, dec in PAIRS:
        ndx = dec.find(i)
        if ndx != -1:
            mapping[enc[ndx]] = i
            #print "%s -> %s" % (i, enc[ndx],)
            break

mapping['z'] = 'q'
mapping['q'] = 'z'
mapping[' '] = ' '

import sys

cnt = int(sys.stdin.readline())
for i in range(cnt):
        ln = sys.stdin.readline().strip()
        encoded = ""
        for k in ln:
                encoded += mapping[k]
        print "Case #%d: %s" % (i + 1, encoded)
