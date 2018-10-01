#! /usr/bin/env python

from sys import stdin

ntest = input()

d = {' ': ' ',
     'a': 'y',
     'b': 'h',
     'c': 'e',
     'd': 's',
     'e': 'o',
     'f': 'c',
     'g': 'v',
     'h': 'x',
     'i': 'd',
     'j': 'u',
     'k': 'i',
     'l': 'g',
     'm': 'l',
     'n': 'b',
     'o': 'k',
     'p': 'r',
     'q': 'z',
     'r': 't',
     's': 'n',
     't': 'w',
     'u': 'j',
     'v': 'p',
     'w': 'f',
     'x': 'm',
     'y': 'a',
     'z': 'q'}

for test in range(ntest):
    s = stdin.readline().strip()
    o = ''.join([d[i] for i in s])
    print "Case #%d: %s" % (test+1, o)