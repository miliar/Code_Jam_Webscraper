#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2012.04.13

import re
import string

# "The first line of the input gives the number of test cases, T. T
# test cases follow, one per line."
T = int(raw_input())
sentences = []
for _ in range(T):
    sentences.append(raw_input())

def key_gen():
    d = {}
    tups = [
        ("ejp mysljylc kd kxveddknmc re jsicpdrysi",
         "our language is impossible to understand"),
        ("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
         "there are twenty six factorial possibilities"),
        ("de kr kd eoya kw aej tysr re ujdr lkgc jv",
         "so it is okay if you want to just give up")
        ]
    for (k, v) in tups:
        for i in range(len(k)):
            d[k[i]] = v[i]
    d.update({'q': 'z', 'z': 'q'})
    return d

DIC = key_gen()
def english_to_googlese(string):
    return ''.join(DIC[s] for s in string)

for case in range(len(sentences)):
    s = english_to_googlese(sentences[case])
    print "Case #%d: %s" % (case+1, s)
