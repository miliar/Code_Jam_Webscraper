
import sys

if __name__=='__main__':
	input = sys.stdin
	output = open('rez.txt', 'w')
	t = int(input.readline())
	print t
	for _t in xrange(t):
		line = map(int, input.readline().strip().split(' '))
		(n, s, p) = line[:3]
		sums = line[3:]
		rez = 0
		down = 3 * p - 3
		sdown = 3 * p - 5
		if sdown < 0:
			sdown = 0
		if down < 0:
			down = 0
		print p, sdown, down
		for i in sums:
			if i > down:
				rez += 1
				continue
			if s > 0 and i > sdown:
				s -= 1
				rez += 1
		if p == 0:
			rez = n
		output.write('Case #%d: %d\n' % (_t+1, rez))
		print n, s, p, sums

