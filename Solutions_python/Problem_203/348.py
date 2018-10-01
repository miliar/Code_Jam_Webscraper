def put(i, j, R, C) :
    global grid
    if (j-1 >=0 and grid[i][j-1] != '?') :
        grid[i][j] = grid[i][j-1]
    elif (j+1 < C and grid[i][j+1] != '?') :
        grid[i][j] = grid[i][j+1]

def put2(i, j, R, C) :
    global grid
    if (i+1 < R and grid[i+1][j] != '?') :
       grid[i][j] = grid[i+1][j]
    elif (i-1 >=0 and grid[i-1][j] != '?') :
        grid[i][j] = grid[i-1][j]    
        
T = int(input())
for case in range(T) :
    L = input().split(" ")
    R, C = int(L[0]), int(L[1])
    grid = []
    for i in range (R) :
        grid.append(list(input()))
    for k in range (C):
        for i in range (R) :
            for j in range (C) :
                if grid[i][j] == '?' :
                    put(i, j, R, C)
    for k in range (C):
        for i in range (R) :
            for j in range (C) :
                if grid[i][j] == '?' :
                    put2(i, j, R, C)                
    print("Case #", case+1, ":", sep = "")
    for row in grid :
        print("".join(row))
