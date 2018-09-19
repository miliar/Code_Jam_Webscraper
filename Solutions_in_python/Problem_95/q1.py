import sys

input = sys.stdin.read().splitlines()

fmap = {
	'a': 'y',
	'b': 'n',
	'c': 'f',
	'd': 'i',
	'e': 'c',
	'f': 'w',
	'g': 'l',
	'h': 'b',
	'i': 'k',
	'j': 'u',
	'k': 'o',
	'l': 'm',
	'm': 'x',
	'n': 's',
	'o': 'e',
	'p': 'v',
	'q': 'z',
	'r': 'p',
	's': 'd',
	't': 'r',
	'u': 'j',
	'v': 'g',
	'w': 't',
	'x': 'h',
	'y': 'a',
	'z': 'q',
	' ': ' '
}

rmap = dict(zip(fmap.values(), fmap.keys()))

for n in range(1, int(input[0])+1):
	print "Case #%d: %s" % (n, ''.join([rmap[letter] for letter in input[n]]))