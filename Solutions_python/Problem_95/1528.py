import sys

raw_string = """
ejp mysljylc kd kxveddknmc re jsicpdrysi	our language is impossible to understand
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd	there are twenty six factorial possibilities
de kr kd eoya kw aej tysr re ujdr lkgc jv	so it is okay if you want to just give up
"""

mappings = {'z':'q', 'q':'z'}
for m in raw_string.split('\n'):
	ab = m.split('\t')
	for i in xrange(len(ab[0])):
		mappings[ab[0][i]] = ab[1][i]

assert len(sorted(mappings)) == 27

line_count = int(sys.stdin.readline())

for case_num in xrange(line_count):
	line_text = sys.stdin.readline().strip('\r\n')
	line_chars = []
	for c in line_text:
		line_chars.append(mappings[c])
	print 'Case #%d: %s' % (case_num+1, ''.join(line_chars))
