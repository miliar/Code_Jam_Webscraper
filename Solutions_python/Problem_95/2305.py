cases = int(raw_input())

MAP = {}

messages = [('ejp mysljylc kd kxveddknmc re jsicpdrysi', 'our language is impossible to understand'),
		    ('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'there are twenty six factorial possibilities'),
		    ('de kr kd eoya kw aej tysr re ujdr lkgc jv', 'so it is okay if you want to just give up')]

# hints
MAP['z'] = 'q'
MAP['q'] = 'z'
			
for (s, t) in messages:
	for (c1, c2) in zip(s, t):
		MAP[c1] = c2
		
def translate(text):
	return "".join([MAP[c] for c in text])
		  
for i in range(cases):
	line = raw_input().strip()
	print "Case #%d: %s" % (i + 1, translate(line))