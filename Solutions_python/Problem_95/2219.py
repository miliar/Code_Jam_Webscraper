#!/usr/bin/env python

from sys import stdin

sample_in = [
        "ejp mysljylc kd kxveddknmc re jsicpdrysi",
        "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
        "de kr kd eoya kw aej tysr re ujdr lkgc jv",
        ]

sample_out = [
        "our language is impossible to understand",
        "there are twenty six factorial possibilities",
        "so it is okay if you want to just give up",
        ]

mapping = {}

for (line_in, line_out) in zip(sample_in, sample_out):
    for (char_in, char_out) in zip(line_in, line_out):
        mapping[char_in] = char_out

mapping['q'] = 'z'
mapping['z'] = 'q'
mapping[' '] = ' '

T = int(stdin.readline())

for CASE in xrange(1,T+1):
    l = stdin.readline().strip()
    print "Case #%d: %s" % (CASE, "".join([mapping[c] for c in l]))
