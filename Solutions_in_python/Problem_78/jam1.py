def gcd(a,b):
	if a > b:
		return gcd(b, a)
	if a == 0:
		return b
	return gcd(b % a, a)

def frac(percent):
	g = gcd(percent, 100)
	return 100 / g

f = open('A-large.in')
tests = int(f.readline())
output = ''
for t in xrange(tests):
	a = f.readline().split(' ')[:3]
	a = [int(i) for i in a]
	n, pd, pg = tuple(a)
	if pg == 0:
		result = pd == 0
	elif pg == 100:
		result = pd == 100 
	else:
		dplay = frac(pd)
		result = dplay <= n
	output += 'Case #' + str(t + 1) + ': ' + ('Possible' if result else 'Broken') + '\n'

f.close()
f = open('output1.txt', 'w')
print output
f.write(output)
f.close()