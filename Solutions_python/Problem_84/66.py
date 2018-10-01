fin = file("A-large.in", "rU")
fout = file("A-large.out", "w")

nruns = int(fin.readline().strip())
for i in xrange(nruns):
    line = fin.readline().strip().split()
    nrows = int(line[0])
    ncols = int(line[1])

    grid = []

    for j in xrange(nrows):
        grid.append(list(fin.readline().strip()))

    impflag = 0
    for j in xrange(nrows):
        for k in xrange(ncols):
            #print j, k, grid[j][k]
            if grid[j][k] == '#': #blue tile
                
                #check surrounding
                if k+1 >= ncols or grid[j][k+1] != '#':
                    impflag = 1
                if j+1 >= nrows or grid[j+1][k] != '#':
                    impflag = 1
                if k+1 >= ncols or j+1 >= nrows or grid[j+1][k+1] != '#':
                    impflag = 1
                if impflag == 1:
                    break
                #replace
                grid[j][k] = '/'
                grid[j][k+1] = '\\'
                grid[j+1][k] = '\\'
                grid[j+1][k+1] = '/'
        if impflag == 1:
            break
    
    if impflag == 1:
        result = 'Impossible'
    else:
        result = ''
        for row in grid:
            result += ''.join(row) + '\n'
        result = result.strip()
    strout = "Case #" + str(i+1) + ":\n" + str(result) + "\n"
    #print strout
    fout.write(strout)
fin.close()
fout.close()
