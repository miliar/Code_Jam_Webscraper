INPUT_FILE = 'inputs/C-small-attempt1.in'
OUTPUT_FILE = 'outputs/C-small-attempt1.out'

f_in = open(INPUT_FILE, 'r')
f_out = open(OUTPUT_FILE, 'w+')

C = int(f_in.readline())
for c in range(C):
    #init grid
    grid = []
    for i in range(100):
        row = []
        for j in range(100):
            row.append(0)
        grid.append(row)
    
    # filling grid with bacteria
    R = int(f_in.readline())
    for r in range(R):
        X1, Y1, X2, Y2 = [int(i) for i in f_in.readline().split()]
        for j in range(Y1 - 1, Y2):
            for i in range(X1 - 1, X2):
                grid[j][i] = 1
    numberOfBacteria = 0
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if (grid[j][i] == 1):
                numberOfBacteria += 1
    
                
    # simulation
    numberOfSeconds = 0
    while numberOfBacteria > 0:
        for j in range(len(grid) - 1, -1, -1):
            for i in range(len(grid[j]) - 1, -1, -1):
                if grid[j][i] == 1 and (j == 0 or grid[j - 1][i] == 0) and (i == 0 or grid[j][i - 1] == 0):
                    grid[j][i] = 0
                    numberOfBacteria -= 1
                elif grid[j][i] == 0 and (j != 0 and grid[j - 1][i] == 1) and (i != 0 and grid[j][i - 1] == 1):
                    grid[j][i] = 1
                    numberOfBacteria += 1
        numberOfSeconds += 1
    strRes = "Case #" + str(c + 1) + ": " + str(numberOfSeconds)
    f_out.write(strRes + "\n")
    print(strRes) 
    
f_in.close()
f_out.close()
