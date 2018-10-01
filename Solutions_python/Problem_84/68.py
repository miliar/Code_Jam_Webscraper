fname = "A-large"
fin = open(fname + '.in', 'r')
fout = open(fname + '.out', 'w')

T = int(fin.readline())
for i in range(T):
    R, C = [int(x) for x in fin.readline().split()]
    solveable = True

    grid = [[tile for tile in fin.readline()[:-1]] for x in range(R)]

    for r in range(1,R):
        for c in range(1,C):
            if grid[r][c] == '#':
                if grid[r-1][c] == '#' and grid[r][c-1] == '#' and grid[r-1][c-1] == '#':
                    grid[r][c] = '/'
                    grid[r-1][c] = '\\'
                    grid[r][c-1] = '\\'
                    grid[r-1][c-1] = '/'

    for line in grid:
        if '#' in line:
            solveable = False

    fout.write('Case #{}:\n'.format(i+1))
    if solveable:
        for line in grid:
            fout.write(''.join(line) + '\n')
    else:
        fout.write('Impossible\n')
    print "Case", i+1, "finished"

fin.close()
fout.close()
    
