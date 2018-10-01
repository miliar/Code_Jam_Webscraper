mapping = {}

mapping['\n']= ''
mapping[' '] = ' '
mapping['a'] = 'y'
mapping['b'] = 'h'
mapping['c'] = 'e'
mapping['d'] = 's'
mapping['e'] = 'o'
mapping['f'] = 'c'
mapping['g'] = 'v'
mapping['h'] = 'x'
mapping['i'] = 'd'
mapping['j'] = 'u'
mapping['k'] = 'i'
mapping['l'] = 'g'
mapping['m'] = 'l'
mapping['n'] = 'b'
mapping['o'] = 'k'
mapping['p'] = 'r'
mapping['q'] = 'z'
mapping['r'] = 't'
mapping['s'] = 'n'
mapping['t'] = 'w'
mapping['u'] = 'j'
mapping['v'] = 'p'
mapping['w'] = 'f'
mapping['x'] = 'm'
mapping['y'] = 'a'
mapping['z'] = 'q'

f = open("input")

nbTestCase = int(f.readline())

for i in range(0, nbTestCase):
	message = f.readline()
	translation = ""
	for c in message:
		translation = translation + mapping[c]
	print("Case #%d: %s" % (i + 1, translation))



