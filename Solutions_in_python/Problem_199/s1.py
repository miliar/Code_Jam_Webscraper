fin = open('input.in','r')
fout = open('output.out','w')

lines = [line[:-1] for line in fin]

T = int(lines[0])
for cT in range(1,T + 1):
	inputs = lines[cT].split()
	cakes = [1 if c == '+' else -1 for c in inputs[0]]
	window = int(inputs[1])
	sol = 0
	for (i, c) in enumerate(cakes):
		if c == -1:
			if i + window - 1 < len(cakes):
				sol += 1
				for w in range(window):
					cakes[i + w] = -cakes[i + w]
			else:
				sol = 'IMPOSSIBLE'
				break
	fout.write('Case  #' + str(cT) + ': ' + str(sol) + '\n')
