from fractions import gcd
inf  = open('B-large.in', 'r')
out  = open('B.out', 'w')

s = inf.readline()
i=0
for line in inf:
	i = i + 1
	m = line.split()
	m.pop(0)
	k = int(m.pop())
	res = k-int(m.pop())
	for tek in m:
		res=gcd(res,k-int(tek))
	ans = (k/res)*res-k
	while ans < 0:
		ans += res
	print >>out, 'Case #' + str(i) + ': ' + str(ans)
	
