from math import *
inf = open("file.in")
ouf = open("file.out","w")
counttests = int(inf.readline().split()[0])
case = 0
def answer(x):
	global case, counttests
	if case > counttests:
		exit
	case += 1
	print >>ouf, "Case #"+str(case)+": "+str(x)
	print "Case #"+str(case)+": "+str(x)

for iii in xrange(counttests):
	n,k,b,t = map(int, inf.readline().split())
	x = map(int, inf.readline().split())
	v = map(int, inf.readline().split())
	tt = [0]*n;
	for i in xrange(n):
		if x[i]+v[i]*t>=b:
			tt[i] = 1
		else:
			print i
	print tt
	i = n-1
	ok = 0
	res = 0
	while ok < k and i >= 0:
		if tt[i] == 1:
			ok+=1
		else:
			res+=k-ok
		i -= 1
	if ok < k:
		answer('IMPOSSIBLE')
	else:
		answer(res)
