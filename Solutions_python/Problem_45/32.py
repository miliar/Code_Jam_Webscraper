from itertools import permutations as perms
v = [[int(n) for n in line.strip().split()] for line in open('c.in','r').readlines()]

nt = v[0][0]
v = v[1:]

#print(v)

out = open('c.out', 'w')

P, Q = 0, 0

def cost(p):
	s = 0
	x = [1] * P
	for i in p:
#		print(i, P)
		i -= 1
		x[i] = 0
		j = 1
		while i + j < P:
			if x[i + j] == 0:
				break
			j += 1
		j -= 1
#		print(j)
		s += j
		j = 1
		while i - j >= 0:
			if x[i - j] == 0:
				break
			j += 1
		j -= 1
#		print(j)
		s += j
#	print(p, s, x)
	return s

case = 0
while case < nt:
	case += 1
	P, Q = v[0]
	t = v[1]
	v = v[2:]
	r = Q * P
#	print(P, Q)
	for p in perms(t):
		r = min(r, cost(p))
	print("Case #%d: %d" % (case, r), file = out)


