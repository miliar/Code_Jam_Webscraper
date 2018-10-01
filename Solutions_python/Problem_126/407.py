thefile = "A-small-attempt0"
outputfile = open(thefile+".out", "w")

#with open(thefile+".in") as f:
#	ff = [[int(x) for x in line.split()] for line in f]

with open(thefile+".in") as f:
	ff = [[x for x in line.split()] for line in f]

#for i in range(1,ff[0][0]+1):
#	ff[i].pop(0)
#	ans = safe(ff[i])
#	outputfile.write("Case #%i: %s\n" % (i, ' '.join([str(ci) for ci in ans])))

vowels = ['a','e','i','o','u']
	
def test(sub, n):
	count = 0
	for i in xrange(len(sub)):
		if sub[i] not in vowels:
			count += 1
		else:
			count = 0
		if count == n:
			return 1
	return 0

def solve(name,n):
	L = len(name)
	substrings = []
	for i in xrange(L):
		for j in xrange(i+1,L+1):
			substrings.append(name[i:j])
	ans = 0
	for x in substrings:
		ans += test(x,n)
	return ans

T = int(ff[0][0])
for i in range(1,T+1):
	n = int(ff[i][1])
	name = ff[i][0]
	outputfile.write("Case #%i: %i\n" % (i, solve(name,n)))
