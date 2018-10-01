#!/usr/bin/env python2
import sys, os
# Cases
t = int(sys.stdin.readline())
sbox = {' ': ' ', 
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
'z': 'q',
'\n': ''
}

for i in xrange(t):
	line = sys.stdin.readline()
	cleartext = ''
	for l in range(len(line)):
		cleartext += sbox.get(line[l], line[l])
	print "Case #%d: %s" % (i+1, cleartext)
