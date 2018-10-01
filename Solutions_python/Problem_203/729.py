def cakeSplit(grid, row, col):
    emptyRows = 0
    filled = False
    for r in range(row):
        empty = 0
        seen = '?'
        for c in range(col):
            if grid[r][c] == '?' and seen == '?':
                empty += 1
            elif grid[r][c] != '?' and empty > 0:
                seen = grid[r][c]
                for i in range(empty):
                    grid[r][i] = seen
                empty = 0
            elif grid[r][c] != '?' and empty == 0:
                seen = grid[r][c]
            elif grid[r][c] == '?' and seen != '?':
                grid[r][c] = seen
        if seen == '?' and filled == False:
            emptyRows += 1
        elif seen == '?' and filled == True:
            grid[r] = grid[r - 1]

        elif seen != '?' and filled == False:
            for i in range(emptyRows):
                grid[i] = grid[r]
            filled = True
    return grid

t = int(input())
for i in range(1, t+1):
    row, col = map(int, input().split(" "))
    grid = []
    for r in range(row):
        newRow = str(input())
        rowList = []
        for c in newRow:
            rowList.append(c)
        grid.append(rowList)
    result = cakeSplit(grid, row, col)
    print("Case #{}:".format(i))
    for rr in range(row):
        s = ''
        for cc in range(col):
            s += result[rr][cc]
        print(s)