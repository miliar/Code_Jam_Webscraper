#! /usr/bin/python2

def solve():
	n = input()
	candies = map(int,raw_input().split())
	xor = reduce(lambda x,y: x^y, candies)
	if xor == 0: print sum(candies)-min(candies)
	else: print 'NO'

if __name__ == '__main__':
	t = input()
	for i in range(t):
		print 'Case #%d:' % (i+1),
		solve()
