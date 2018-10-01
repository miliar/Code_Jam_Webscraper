import sys
import itertools

file = open(sys.argv[1])
out = open('out.txt', 'w')

N = int(file.readline())
print 'Total ', N, ' cases'

case = 1

def add_without_carry(X):
	sum = 0
	for val in X:
		sum = sum ^ val
#		print val, sum ^ val
	return sum

while case <= N:
#	print case
	final = 0
	m = int(file.readline())
	values = map(lambda x: int(x), file.readline().split())
#	print values
	limit = 2**m
	i = 1
	success = False
#	print 'Total subsets = ', limit
	while i < limit:
		#i denotes the subset
		num = i
		j = 0
		S = []
		P = []
		while num > 0:
			if num & 1:
				S.append(values[j])
			else:
				P.append(values[j])
			num = num >> 1
			j += 1
		i += 1
		if sum(S) <= final:
			continue
		while j < m:
			P.append(values[j])
			j += 1

		if len(S) == 0 or len(P) == 0:
			continue
		if add_without_carry(S) == add_without_carry(P):
			val = max(sum(S), sum(P))
			success = True
			if final < val:
				final = val

	if not success:
		res = 'NO'
	else:
		res = str(final)
#	print case, res
	out.write('Case #' + str(case) + ': ' + res + '\n')
	case += 1
