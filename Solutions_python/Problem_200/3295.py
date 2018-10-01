import pdb

def solveproblem(w):
	N = len(w)
	prev = int(w[0])
	i = 0
	cont = 0
	# pdb.set_trace()
	for j in w[1:]:
		i = i + 1
		curr = int(j)
		if curr < prev and prev > 1:
			return w[:cont] + str(prev-1) + '9'*(i-cont-1) + '9'*(N-i)
		elif curr < prev and prev == 1:
			return w[:cont] + '9'*(i-cont-1) + '9'*(N-i)
		elif curr > prev:
			cont = i
			prev = int(j)
	return w


def solvecases():
	n = int(raw_input())
	for j in range(n):
		num = raw_input()
		print "Case #" + str(j+1) + ": " + solveproblem(num)
		
solvecases()