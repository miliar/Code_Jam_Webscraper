from sys import stdin

def solve():
	N, K = [int(x) for x in stdin.readline().split(' ')]
	
	if K % (2**N) == 2**N-1:
		print "ON"
	else:
		print "OFF"
	
T = int(stdin.readline())
for case in range(T):
	print 'Case #%d:' % (case+1), 
	solve()
