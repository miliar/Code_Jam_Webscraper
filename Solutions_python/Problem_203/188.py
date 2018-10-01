import gcj

#gcj.set_sample()

ifile, ofile = gcj.get_files('A')

T = int(ifile.readline().strip())
for t in range(T):
    (R, C) = list(map(int, ifile.readline().strip().split()))
    field = []
    for row in range(R):
        field.append(list(ifile.readline().strip()))

    empty_rows = []
    for i in range(R):
        row = field[i]
        #find first
        j = 0
        while j < C:
            if row[j] == '?':
                j = j + 1
            else:
                break

        if j < C:
            #fill first
            for jj in range(j):
                row[jj] = row[j]
            current = row[j]
            for jj in range(j, C):
                if row[jj] == '?':
                    row[jj] = current
                else:
                    current = row[jj]
        else:
            empty_rows.append(i)

    #print(empty_rows)
    for e in empty_rows:
        #find next not empty
        ee = e + 1
        while ee < R:
            if not ee in empty_rows:
                break
            else:
                ee += 1
        if ee == R:
            #copy previous
            for i in range(e, R):
                for j in range(C):
                    field[i][j] = field[e - 1][j]
        else:
            #copy found up
            for i in range(e, ee):
                for j in range(C):
                    field[i][j] = field[ee][j]

        
    ans = "\n" + "\n".join([''.join(r) for r in field])
    #for 

    gcj.print_answer(ofile, t, ans)