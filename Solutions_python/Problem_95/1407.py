import re
#import cj

tr = {}

s0 = 'yeqz'
s1 = 'ejp mysljylc kd kxveddknmc re jsicpdrysi'
s2 = 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
s3 = 'de kr kd eoya kw aej tysr re ujdr lkgc jv'

s = s0 + s1 + s2 + s3

t0 = 'aozq'
t1 = 'our language is impossible to understand'
t2 = 'there are twenty six factorial possibilities'
t3 = 'so it is okay if you want to just give up'

t = t0 + t1 + t2 + t3

for (s_, t_) in zip(s, t):
	if (s_ in tr and tr[s_] != t_):
		print 'Overwriting!'
	tr[s_] = t_
	#print s_ + '->' + t_

f = open('A-small-attempt0.in')
T = int(f.readline())
for i in xrange(T):
	line = f.readline()
	line = re.sub('\n','',line)
	o = ''
	for c in line:
		o += tr[c]
	print 'Case #%d: %s' % (i+1, o)



