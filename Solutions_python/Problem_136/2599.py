'''python template for google code jam
'''

import math
import sys

# sys.stdin = open('1.in', 'r')
# sys.stdout = open('1.out', 'w')

#sys.stdin = open('B-small-attempt0.in', 'r')
#sys.stdout = open('B-small-attempt0.out', 'w')

sys.stdin = open('B-large.in', 'r')
sys.stdout = open('B-large.out', 'w')

# input
# a, b = map(int, sys.stdin.readline().split())

def ComputeN(c, f, x):
	return x / c - 2 / f - 1

def ComputeResult(c, f, x, n):
	res = 0
	for i in range(int(n)):
		res += c / (2 + i * f)
	res += x / (2 + n * f)
	return res

t = int(sys.stdin.readline())
for cc in range(1, t+1):
	c, f, x = map(float, sys.stdin.readline().split())
	n = ComputeN(c, f, x)
	n = int(n)
	if n < 0:
		n = 0
	ans = ComputeResult(c, f, x, n)
	ans2 = ComputeResult(c, f, x, n+1)
	answer = ans if ans < ans2 else ans2
	sys.stdout.write('Case #' + str(cc) + ': ' + str(answer) + '\n')
  
  