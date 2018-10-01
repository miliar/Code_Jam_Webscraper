import sys

G2E = {
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
	' ': ' ',
	'\n': '\n'
}

T = int(sys.stdin.readline())
for i in range(1, T + 1):
	a = sys.stdin.readline()
	print("Case #" + str(i) + ": ", end="")
	for c in a:
		print(G2E[c], end="")
