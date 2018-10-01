import sys

inp = open(sys.argv[1],"r")
outp = open(sys.argv[2],"w")
case_count = int(inp.readline())
for case_num in range(1,case_count+1):
	NM = map(lambda s:int(s),inp.readline().strip().split())
	assert( len(NM)==2)
	N = NM[0]
	M = NM[1]
	table = []
	for i in range(N):
		row = map(lambda s:int(s),inp.readline().strip().split())
		assert(len(row)==M)
		table.append( row )

	possible = True
	for i in range(N):
		for j in range(M):
			height = table[i][j]
			vertical_ok = True
			for k in range(N):
				if not (table[k][j] <= height):
					vertical_ok = False
					break
			horizontal_ok = True
			for k in range(M):
				if not (table[i][k] <= height):
					horizontal_ok = False
					break
			if not(vertical_ok or horizontal_ok):
				possible = False
				break
		if not possible:
			break
	if possible:
		outp.write("Case #%i: YES\n"%(case_num,))
	else:
		outp.write("Case #%i: NO\n"%(case_num,))