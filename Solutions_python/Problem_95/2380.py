import operator
ky = dict ()

def trans (s, t):
	for i in range (len (s)):
		ky [s [i]] = t [i]

a  = "our language is impossible to understand"
a2 = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
b  = "there are twenty six factorial possibilities"
b2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
c  = "so it is okay if you want to just give up"
c2 = "de kr kd eoya kw aej tysr re ujdr lkgc jv"
d  = "azoq"
d2 = "yqez"

strs = [(a2, a), (b2, b), (c2, c), (d2, d)]

for x in strs:
	trans (x [0], x [1])

lines = open ("input.txt").read ().split ('\n')[:-1]
N = int (lines [0])
result = []

for i in range (1, N+1):
	tr = ""
	for c in lines [i]:
		tr += ky [c]
	print "Case #%d: %s" % (i, tr)
