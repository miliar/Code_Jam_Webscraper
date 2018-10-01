
def gcd2(a, b):
	while b != 0:
		(a, b) = (b, a%b)
	return a

def gcd(l):
	a = l[0]
	for b in l[1:]:
		a = gcd2(a, b)
	return a

	"""if len(l) == 1:
		return l[0]
	else:
		a = l[0]
		b = gcd(l[1:])
		while b != 0:
			(a, b) = (b, a%b)
		return a"""


fin = open('B-large.in', 'r')
fout = open('B-large.out', 'w')

T = int(fin.readline())
for t in range(0, T):
	nums = map(int, fin.readline().split()[1:])
	diffs = [x-y for x in nums for y in nums if x-y>0]
	g = gcd(diffs)
	
	same_diff = nums[0]%g
	for num in nums:
		if num%g != same_diff:
			print "problem: %d != %d" % (num%g, same_diff)
	
	fout.write("Case #%d: %d\n" % (t+1, (g - nums[0]%g)%g))
