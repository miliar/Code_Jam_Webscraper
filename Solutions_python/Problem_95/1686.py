#!/bin/python

import sys

assoc = {
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
'z': 'q'
}

def translate(string, i):
    res = ""
    for char in string:
        if char in assoc:
            res += '%c' % assoc[char]
        else:
            res += '%c' % char
    print "Case #%d: %s" % (i+1, res),

fs = open(sys.argv[1])
line = fs.readline()
nb_line = int(line)
for i in range(nb_line):
    translate(fs.readline(), i)
