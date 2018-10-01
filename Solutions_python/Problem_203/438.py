# David Mende
# Google Code Jam 2017
# Round 1a
# Problem A

def output(cake):
	newcake = []
	for row in cake:
		s = row.replace('?','')
		if s:
			char = s[0]
			newrow = ''
			for c in row:
				if c == '?':
					newrow += char
				else:
					newrow += c
					char = c
			newcake.append(newrow)
		else:
			newcake.append('')
	for row in newcake:
		if row:
			srow = row
			break
	res = []
	for row in newcake:
		if row:
			res.append(row)
			srow = row
		else:
			res.append(srow)
	return res

for i in range(int(input())):
	r,c = [int(a) for a in input().split()]
	cake = [input() for _ in range(r)]
	print('Case #'+str(i+1)+':')
	for row in output(cake):
		print(row)
