def cookieClicker(C, F, X, rate, a, b):
	s1 = C / rate
	s2 = X / rate

	if b < a + s2:
		return b
	else:
		return a + cookieClicker(C, F, X, rate + F, s1, s2)

def iter(C, F, X):
	a = C / 2
	b = X / 2
	rate = 2 + F
	time = 0

	while True:
		s1 = C / rate
		s2 = X / rate

		if b < a + s2:
			return b + time
		else:
			time += a
			rate += F
			a = s1
			b = s2
	
from sys import stdin

input = stdin.read().split('\n')

for t in range(int(input[0])):
	C, F, X = map(float, input[t+1].split())

	print "Case #{0}: {1:.7f}".format(t+1, iter(C, F, X))#cookieClicker(C, F, X, 2+F, C/2, X/2))