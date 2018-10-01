T=int(input())
for testcase in range(1,T+1):
	N,M = [int(x) for x in input().split()]
	grid = [['.']*(N+1) for i in range(N+1)]
	#print(grid)
	rows, cols, crossplus, crossminus = set(), set(), set(), set()
	for i in range(M):
		model = input().split()
		typ, r, c = model[0], int(model[1]), int(model[2])
		grid[r][c] = typ
		if typ=='o' or typ=='x':
			rows.add( r )
			cols.add( c )
		if typ=='o' or typ=='+':
			crossplus.add( r+c )
			crossminus.add( r-c )
	
	#print(grid)
	#print(rows)
	#print(cols)
	#print(crossplus)
	#print(crossminus)
	
	field=[(i,j) for i in range(1,N+1) for j in range (1,N+1)]
	
	circle, plus, cross = [], [], []
	for i,j in sorted(field, key=lambda x: min([x[0]-1, x[1]-1, N-x[0], N-x[1]])):
		if grid[i][j]=='o':
			pass
		if grid[i][j]=='+':
			if i not in rows and j not in cols:
				circle.append( (i,j) )
				rows.add(i)
				cols.add(j)
				crossplus.add(i+j)
				crossminus.add(i-j)
				grid[i][j]='o'
		if grid[i][j]=='x':
			if i+j not in crossplus and i-j not in crossminus:
				circle.append( (i,j) )
				rows.add(i)
				cols.add(j)
				crossplus.add(i+j)
				crossminus.add(i-j)
				grid[i][j]='o'
		if grid[i][j]=='.':
			if i not in rows and j not in cols and i+j not in crossplus and i-j not in crossminus:
				circle.append( (i,j) )
				rows.add(i)
				cols.add(j)
				crossplus.add(i+j)
				crossminus.add(i-j)
				grid[i][j]='o'
			elif i not in rows and j not in cols:
				cross.append( (i,j) )
				rows.add(i)
				cols.add(j)
				grid[i][j]='x'
			elif i+j not in crossplus and i-j not in crossminus:
				plus.append( (i,j) )
				crossplus.add(i+j)
				crossminus.add(i-j)
				grid[i][j]='+'
	
	value={'.':0, 'o':2, 'x':1, '+':1}
	
	score = 0;
	for i in range(1,N+1):
		for j in range (1,N+1):
			score+= value[grid[i][j]]
					
	print("Case #"+ str(testcase)+ ":", score, len(cross)+len(plus)+len(circle))
	for i,j in circle:
		print('o', i, j)
	for i,j in plus:
		print('+', i, j)
	for i,j in cross:
		print('x', i, j)