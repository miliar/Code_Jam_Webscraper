code = {' ': ' ', 'a': 'y', 'c': 'f', 'b': 'n', 'e': 'c', 'd': 'i', 'g': 'l', 'f': 'w', 'i': 'k', 'h': 'b', 'k': 'o', 'j': 'u', 'm': 'x', 'l': 'm', 'o': 'e', 'n': 's', 'q': 'z', 'p': 'v', 's': 'd', 'r': 'p', 'u': 'j', 't': 'r', 'w': 't', 'v': 'g', 'y': 'a', 'x': 'h', 'z': 'q'}
inverted = {}
for s in code:
	inverted[code[s]] = s

import sys

T = int(sys.stdin.readline())
for i in xrange(T):
	line = sys.stdin.readline()[:-1]
	result = ''.join(map(lambda x: inverted[x], line))
	print "Case #%d: %s" % (i + 1, result)
