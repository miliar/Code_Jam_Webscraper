#!/usr/bin/python

import sys

gdict = {
    ' ' : ' ',
    'a' : 'y',
    'b' : 'h',
    'c' : 'e',
    'd' : 's',
    'e' : 'o',
    'f' : 'c',
    'g' : 'v',
    'h' : 'x',
    'i' : 'd',
    'j' : 'u',
    'k' : 'i',
    'l' : 'g',
    'm' : 'l',
    'n' : 'b',
    'o' : 'k',
    'p' : 'r',
    'r' : 't',
    's' : 'n',
    't' : 'w',
    'u' : 'j',
    'v' : 'p',
    'w' : 'f',
    'x' : 'm',
    'y' : 'a',
}

gdicts = []
gdicts.append(gdict.copy())
gdicts.append(gdict.copy())
gdicts[0]['q'] = 'q'
gdicts[0]['z'] = 'z'
gdicts[1]['q'] = 'z'
gdicts[1]['z'] = 'q'

def translate(string):
    return ''.join(gdicts[1][c] for c in string)

if __name__ == '__main__':
    T = int(raw_input())
    for case in xrange(1, T+1):
        print "Case #{0}: {1}".format(case, translate(raw_input()))

