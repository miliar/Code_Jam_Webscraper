import sys

def solve():
	D = int(s.readline())
	P = map(int, s.readline().split())
	return solverec(P, 0, max(P))

def solverec(P, moves, cutoff):
	if moves >= cutoff:
		return cutoff
	P = sorted(P, reverse=True)
	m = P[0] + moves
	front = P.pop(0)
	P.append(front/2)
	P.append(front/2 + front%2)
	m = min(m, solverec(P, moves+1, m))
	if front == 9:
		P[-1] = 3
		P[-2] = 6
		m = min(m, solverec(P, moves+1, m))
	return m

s = sys.stdin

T = int(s.readline())

for i in range(1,T+1):
	print "Case #%d: %d" % (i, solve())



