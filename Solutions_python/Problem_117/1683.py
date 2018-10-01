
fin = open('quals_B.in')
fout = open('quals_B.out','w')
n_input = int(fin.readline())

for i_input in range(n_input):
    rowcols = [ int(a) for a in fin.readline().split() ]
    n_row = rowcols[0]
    n_col = rowcols[1]

    rows = [ [int(a) for a in fin.readline().split()] for r in range(n_row) ]
    rmaxs = [max(row) for row in rows]
    cmaxs = [max(col) for col in [[row[c] for row in rows] for c in range(n_col)]]
    #print rmaxs
    #print cmaxs

    cando = True
    for r in range(n_row):
        for c in range(n_col):
            if rows[r][c] < rmaxs[r] and rows[r][c] < cmaxs[c]:
                cando = False
                
    fout.write("Case #" + str(i_input+1) + ": ")
    if cando:
        fout.write("YES\n")
    else:
        fout.write("NO\n")
    

fin.close()
fout.close()
