import math
f = open("B-small-attempt3.in", 'r')
ou = open("out", 'w')
inlist = f.readlines()
L = int(inlist[0])
def slnB(D, P):
	ma = max(P)
	mi = ma
	for i in xrange(1, ma + 1):
		sum = i
		for j in xrange(D):
			if P[j] > i:
				if P[j] % i == 0:
					sum += (P[j] / i - 1)
				else:
					sum += (P[j] / i)
		mi = min(mi, sum)
	return str(mi)

row = 1
for i in xrange(L):
	D = int(inlist[row])
	row += 1
	P = [int(ch[0]) for ch in inlist[row].split(' ') if ch != '\n' and ch != '']
	print D, P
	res = slnB(D, P)
	row += 1
	ou.write("Case #" + str(i + 1) + ": " + res + '\n')
f.close()
ou.close()

