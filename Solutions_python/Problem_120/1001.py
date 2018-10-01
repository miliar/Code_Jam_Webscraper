import math
from decimal import *

def main():
	test_cnt = int(raw_input())
	getcontext().prec = 20
	for i in xrange(test_cnt):
		r , t=  [int(x) for x in raw_input().split()]
		y_float = Decimal(math.sqrt(2 * t + r * r - r + 0.25)) - Decimal(0.5)
		y = math.floor(y_float)
		y = long(y)
		while True:
			if (y % 2) == (r % 2):
				y -= 1
			else:
				if ((y + r) * (y - r + 1)) > (2 * t):
					y -= 2
					continue
				print 'Case #%d: %d' % (i + 1, (y - r + 1) / 2)
				break

if __name__ == '__main__':
	main()