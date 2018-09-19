import math

def AllEquals(pal2):
	val = 1
	primer = pal2[0]
	for w in pal2:
		if (w != primer):
			val = 0
	return val

for case in xrange(input()):
	sol = 'Fegla Won'
	N = int(input())
	pal = []
	for i in xrange(N):
		pal.append(raw_input())

#	print pal

	matriz = []
	pal2 = []
	for w in pal:
		nums = []
		w2 = ''
		iguales = 1
		for i in xrange(len(w) - 1):
			if (w[i] != w[i+1]):
				w2 += w[i]
				nums.append(iguales)
				iguales = 1
			else:
				iguales += 1
		if (len(w) > 1):
			if (w[-1] != w[-2]):
				iguales = 1
		nums.append(iguales)
		w2 += w[-1]
		pal2.append(w2)
		matriz.append(nums)

#	print pal2
#	print matriz
	if (AllEquals(pal2) == 1):
		num_mov = 0
		for i in xrange(len(matriz[0])):
			media = 0
			for j in xrange(N):
				media += matriz[j][i]
			media = int(math.floor(media/N))
			for j in xrange(N):
				num_mov += abs(matriz[j][i] - media)
		sol = str(num_mov)

	print 'Case #%d: %s' % (case+1, sol)
