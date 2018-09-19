from sys import stdin
from string import ascii_lowercase, maketrans

G = {
	'y': 'a',
	'e': 'o',
	'q': 'z'
}

def update(s, g):
	for i in xrange(len(s)):
		old = G.setdefault(s[i], g[i])
		assert old == g[i]

update('ejp mysljylc kd kxveddknmc re jsicpdrysi', 'our language is impossible to understand')
update('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'there are twenty six factorial possibilities')
update('de kr kd eoya kw aej tysr re ujdr lkgc jv', 'so it is okay if you want to just give up')

ascii = set(ascii_lowercase)
G[(ascii - set(G.viewkeys())).pop()] = (ascii - set(G.viewvalues())).pop()
assert len(G) == len(ascii_lowercase) + 1

keys = []
values = []
for k, v in G.iteritems():
	keys.append(k)
	values.append(v)
table = maketrans(''.join(keys), ''.join(values))

lines = iter(stdin)
c = int(next(lines))
for i in xrange(1, c + 1):
	line = next(lines)
	print 'Case #{0}: {1}'.format(i, line.strip().translate(table))