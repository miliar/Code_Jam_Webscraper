#!/usr/bin/python2.7


from sys import stdin, stdout
from string import maketrans

inf, ouf = stdin, stdout
cache = {}


def Googlerese():
    inp = """ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"""
    oup = """our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"""

    g = {}
    for i,j in zip(inp.replace(' ',''), oup.replace(' ','')):
        g[i] = j

    g['q'] = 'z'
    g['z'] = 'q'

    """
    g = {'a': 'y', 'c': 'f', 'b': 'n', 'e': 'c', 'd': 'i', 'g': 'l', 'f': 'w',
            'i': 'k', 'h': 'b', 'k': 'o', 'j': 'u', 'm': 'x', 'l': 'm',
            'o': 'e', 'n': 's', 'q': 'z', 'p': 'v', 's': 'd', 'r': 'p',
            'u': 'j', 't': 'r', 'w': 't', 'v': 'g', 'y': 'a', 'x': 'h',
            'z': 'q'}
    """

    transtable = maketrans(''.join(g.keys()), ''.join(g.values()))

    T = int(inf.readline())

    for X, G in enumerate(inf.readlines(), 1):
        S = G.translate(transtable)
        ouf.write("Case #%d: %s" %(X, S))
        ouf.flush()

Googlerese()

