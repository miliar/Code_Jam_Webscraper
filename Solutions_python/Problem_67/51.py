from copy import deepcopy
run = 'small-attempt2'

inName = 'C-' + run + '.in'
outName = 'C-' + run + '.out'

infile = open(inName,'r')
outfile = open(outName,'w')

cases = int(infile.readline().strip('\n'))

for case in range(1,cases+1):
    print case
    R = int(infile.readline().strip('\n'))
    T = 0
    
    if R == 0:
        outfile.write("Case #" + str(case) + ": 0" + "\n")
    else:
        grid = []
        nextGrid = []
        for i in range(0, 101):
            grid.append([0]*101)
            nextGrid.append([0]*101)
        for r in range(0, R):
            line = infile.readline().strip('\n')
            tokens = line.split()
            X1 = int(tokens[0])
            Y1 = int(tokens[1])
            X2 = int(tokens[2])
            Y2 = int(tokens[3])
            for i in range(X1, X2+1):
                for j in range(Y1, Y2+1):
                    grid[i][j] = 1
        dead = False
        while not dead:
            dead = True
            T += 1
            for i in range(0, 101):
                for j in range(0, 101):
                    if grid[i][j] == 1:
                        if i == 0 and j == 0:
                            nextGrid[i][j] = 0
                        elif i == 0:
                            if grid[i][j-1] == 0:
                                nextGrid[i][j] = 0
                            else:
                                nextGrid[i][j] = 1
                                dead = False
                        elif j == 0:
                            if grid[i-1][j] == 0:
                                nextGrid[i][j] = 0
                            else:
                                nextGrid[i][j] = 1
                                dead = False
                        elif grid[i-1][j] == 0 and grid[i][j-1] == 0:
                            nextGrid[i][j] = 0
                        else:
                            nextGrid[i][j] = 1
                            dead = False
                    if grid[i][j] == 0:
                        if i == 0 or j ==0:
                            nextGrid[i][j] = 0
                        else:
                            if grid[i-1][j] == 1 and grid[i][j-1] == 1:
                                nextGrid[i][j] = 1
                                dead = False
                            else:
                                nextGrid[i][j]=0
            grid = deepcopy(nextGrid)
            
    
    # Code for each case goes here
    
    outfile.write("Case #" + str(case) + ": " + str(T) + "\n")

infile.close()
outfile.close()
