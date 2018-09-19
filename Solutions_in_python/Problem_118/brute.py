import math
l = []
for i in xrange(1,10000001):
	if str(i) == str(i)[::-1] and str(i*i) == str(i*i)[::-1]:
		l = l + [i]
#		print i,' '
def fn(x):
	cnt = 0
	for i in l:
		cnt += 1 if i <= x else 0
	return cnt
T = int(raw_input())
for t in xrange(1, T+1):
	x = raw_input().split()
	a = int(math.sqrt(int(x[0]) - 1))
	b = int(math.sqrt(int(x[1])))
#	print a,' ',b
	print "Case #"+str(t)+": "+str(fn(b) - fn(a))
