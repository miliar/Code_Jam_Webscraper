
voc = {' ': ' ', 'a': 'y', 'b': 'h', 'c': 'e', 'd': 's', 'e': 'o', 'f': 'c', 'g': 'v', 'h': 'x', 'i': 'd', 'j': 'u', 'k': 'i', 'l': 'g', 'm': 'l', 'n': 'b', 'o': 'k', 'p': 'r', 'q': 'z', 'r': 't', 's': 'n', 't': 'w', 'u': 'j', 'v': 'p', 'w': 'f', 'x': 'm', 'y': 'a', 'z': 'q'}

def translate(text):
	trans = []
	for char in text:
		trans.append(voc[char])
	return ''.join(trans)


test_cases = int(raw_input())
for test in xrange(1, test_cases + 1):
	text = raw_input()
	print 'Case #%d: %s' % (test, translate(text))