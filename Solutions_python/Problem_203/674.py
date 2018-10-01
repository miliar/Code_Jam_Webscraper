# Leon Xueliang Liu 2017

with open('A-large.in', 'r') as f:
	content = f.readlines()

T = int(content[0]) # # of cases
data = [[val for val in line.split()] for line in content[1:]]

result = [] # list of results

m = 0
for n in range(T):
	R = int(data[m][0])
	C = int(data[m][1])

	m = m+1

	# begin upright
	begin = []
	for i in range(R):
		row = []
		temp = data[m+i][0]
		for j in range(C):
			row.append(str(temp[j]))
		begin.append(row)


	# sort columns
	mat = []

	for i in range(C):
		col = []
		for j in range(R):
			s = str(begin[j][i])
			if s != '?':
				for k, p in enumerate(col):
					if p == '?':
						col[k] = s
			col.append(s)
		mat.append(col)

	# invert
	new = []
	for i in range(C-1,-1,-1):
		col = []
		for j in range(R-1,-1,-1):
			col.append(mat[i][j])
		new.append(col)

	# sort columns again
	mat = []
	for i in range(C):
		col = []
		for j in range(R):
			s = str(new[i][j])
			if s != '?':
				for k, p in enumerate(col):
					if p == '?':
						col[k] = s
			col.append(s)
		mat.append(col)

	# sort rows
	mat2 = []

	for i in range(R):
		row = []
		for j in range(C):
			s = str(mat[j][i])
			if s != '?':
				for k, p in enumerate(row):
					if p == '?':
						row[k] = s 
			row.append(s)
		mat2.append(row)

	# invert
	new = []
	for i in range(R-1,-1,-1):
		row = []
		for j in range(C-1,-1,-1):
			row.append(mat2[i][j])
		new.append(row)	

	# sort rows again
	ans = []

	for i in range(R):
		row = []
		for j in range(C):
			s = str(new[i][j])
			if s != '?':
				for k, p in enumerate(row):
					if p == '?':
						row[k] = s 
			row.append(s)
		ans.append(row)

	result.append(ans)

	m = m+R

#write to output
with open('A-large.txt','w+') as f:
	for count, ans in enumerate(result):
		f.write("Case #{}:\n".format(count+1))
		for row in ans:
			f.write(''.join(row))
			f.write("\n")
