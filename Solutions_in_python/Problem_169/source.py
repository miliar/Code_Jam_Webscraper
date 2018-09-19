# B small
from decimal import Decimal

def time_required(V, X, Volume, Temp):
	if not (min(X) <= Temp <= max(X)):
		return 'IMPOSSIBLE'
	if len(X) == 1 or X[0] == X[1]:
		return Volume/sum(V)
	T0 = (Temp - X[1])/(X[0] - X[1])*Volume
	T1 = (Temp - X[0])/(X[1] - X[0])*Volume
	return max(T0/V[0], T1/V[1])






#############################################################

inF = open('input.in')
case_sols = []
for case in xrange(int(inF.readline())):
	N, Volume, Temp = inF.readline().split()
	N, Volume, Temp = int(N), Decimal(Volume), Decimal(Temp)
	V, X = [], []
	for source in xrange(N):
		v, x = map(Decimal, inF.readline().split())
		V.append(v)
		X.append(x)
	case_sols.append(time_required(V, X, Volume, Temp))

inF.close()

outF = open('solution.txt', 'w')
for i, sol in enumerate(case_sols, start=1):
	outF.write('Case #{0}: '.format(i) + str(sol) + '\n')

outF.close()