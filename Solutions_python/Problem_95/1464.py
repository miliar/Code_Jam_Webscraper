#!/usr/bin/env python2

replacements = {
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
	'q': 'z', #!
	'r': 't',
	's': 'n',
	't': 'w',
	'u': 'j',
	'v': 'p',
	'w': 'f',
	'x': 'm',
	'y': 'a',
	'z': 'q', #!
	' ': ' ',
}

def solve(text):
	return ''.join([replacements[l] for l in text])

with open('in.txt') as fin:
	with open('out.txt', 'w') as fout:
		T = int(fin.readline().strip())
		for case in xrange(T):
			text = fin.readline().strip()
			print >>fout, 'Case #%d: %s' % (case+1, solve(text))
