import sys

s0 = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""
s1 = """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""

a2z0 = '\n abcdefghijklmnopqrstuvwxyz'
loner = []
a2z1 = ''
for c in a2z0:
#	print c, 
	#print s0.index(c), 
	try:
#		print s1[s0.index(c)]
		a2z1 += s1[s0.index(c)]
	except ValueError:
		loner.append(c)
#		print ' '
		a2z1 += ' '

assert len(loner) in (0,2)

if loner:
	i,j = [a2z0.index(x) for x in loner]
	la2z1 = list(a2z1)
	la2z1[i] = loner[1]
	la2z1[j] = loner[0]
	a2z1 = ''.join(la2z1)
#print a2z0
#print a2z1



#f = open('ok_pair.txt','r')
f = sys.stdin
n = int(f.next())

for i in range(n):
	inp = f.next()
	print "Case #%d: " % (i + 1),
	#print c
	#print [c for c in inp]
	#print [(c in a2z0) for c in inp]
	print ''.join([a2z1[a2z0.index(c)] for c in inp]),
