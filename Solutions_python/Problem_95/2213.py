#!/usr/bin/env python
from collections import defaultdict

def create_mapping(goog, eng):
    '''return the mapping of googlerese characters to english characters.'''
    mapping = {}
    for g, e in zip(goog, eng):
        mapping.update(dict(zip(g, e)))

    return mapping

def solve(goog, m):
    return ''.join(m[c] for c in goog)


if __name__ == '__main__':
    import sys

    goog = [
        'z'
        'y qee',
        'ejp mysljylc kd kxveddknmc re jsicpdrysi',
        'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
        'de kr kd eoya kw aej tysr re ujdr lkgc jv',
    ]
    eng = [
        'q'
        'a zoo',
        'our language is impossible to understand',
        'there are twenty six factorial possibilities',
        'so it is okay if you want to just give up',
    ]

    mapping = create_mapping(goog, eng)

    f = open(sys.argv[1])

    cases = int(f.readline())

    for i in xrange(cases):
        goog = f.readline().strip()
        eng = solve(goog, mapping)
        print "Case #%s: %s" % (i+1, eng)

