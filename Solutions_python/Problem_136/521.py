import sys 
import math

def time(C,F,X,n):
	res = 0
	for i in range(n):
		res += C / (2 + i * F)
	res += X / (2 + n * F)
	return res

T = int(sys.stdin.readline())

for tc in range(T):
	line = map(float, (sys.stdin.readline()).split())
	C = line[0]
	F = line[1]
	X = line[2]
	n = int(max(0, math.ceil( (F * X - C * (F + 2) ) / (F * C) )))
	output = time(C,F,X,n)
	print "Case #" + str(tc + 1) + ": " + str(output)