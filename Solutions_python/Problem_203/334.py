numCases = int(input()) 
for caseNum in range(1, numCases + 1):
    n, m = [int(s) for s in input().split(" ")]
    
    grid = [[s for s in input()] for i in range(n)]
    
    for i in range(n-1):
        for j in range(m):
            if grid[i][j] != '?' and grid[i+1][j] == '?':
                grid[i+1][j] = grid[i][j]
                
                
    for i in range(n-1, 0, -1):
        for j in range(m-1, -1, -1):
            if grid[i][j] != '?' and grid[i-1][j] == '?':
                grid[i-1][j] = grid[i][j]
                
                
    for i in range(n):
        for j in range(m-1):
            if grid[i][j] != '?' and grid[i][j+1] == '?':
                grid[i][j+1] = grid[i][j]
                
                
    for i in range(n-1, -1, -1):
        for j in range(m-1, 0, -1):
            if grid[i][j] != '?' and grid[i][j-1] == '?':
                grid[i][j-1] = grid[i][j]
   
    print("Case #{}:".format(caseNum))
    for line in grid:
        for element in line:
            print(element, end='')
        print()
