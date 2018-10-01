import sys
import psyco
psyco.full()
def dbg(a): sys.stderr.write(str(a))
def readint(): return int(raw_input())
def readfloat(): return float(raw_input())
def readarray(foo): return [foo(x) for x in raw_input().split()]

def gcd(a, b):
	if a < b: (a, b) = (b, a)
	while b > 0:
		a %= b
		(a, b) = (b, a)
	return a

def run_test(test):
	dbg("Test %d\n" % (test + 1))
	a = readarray(int)
	g = abs(a[2] - a[1])
	for i in xrange(3, a[0] + 1):
		g = gcd(g, abs(a[i] - a[i - 1]))
	dbg("%d\n" % g)
	res = (g - (a[1] % g)) % g
	print "Case #%d: %d" % (test + 1, res)

for test in range(readint()):
	run_test(test)

