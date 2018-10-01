def check(mat, w, h):
	bit = []
	for j in range(int(w)):
		tmp = []
		for k in range(int(h)):
			tmp.append(False)
		bit.append(tmp)
	for j in range(int(w)):
		for k in range(int(h)):
			if not bit[j][k]:
				d = int(mat[j][k])
				valid1 = True
				for x in range(int(h)):
					if int(mat[j][x]) > d:
						valid1 = False
						break
				valid2 = True
				for y in range(int(w)):
					if int(mat[y][k]) > d:
						valid2 = False
						break
				if valid1:
					for x in range(int(h)):
						if int(mat[j][x]) == d:
							bit[j][x] = True
				if valid2:
					for y in range(int(w)):
						if int(mat[y][k]) == d:
							bit[y][k] = True
				if not valid1 and not valid2:
					return False
	return True
					

fin = open('b.in', 'r')
fout = open('b.out', 'w')

n = fin.readline()

for i in range(1, int(n)+1):
	wh = fin.readline().strip()
	w, h = wh.split(' ')
	
	mat = []
	for j in range(int(w)):
		mat.append(fin.readline().strip().split(' '))
	if check(mat, w, h):
		fout.write('Case #%d: YES\n' %i)
	else:
		fout.write('Case #%d: NO\n' %i)

fout.close()
		