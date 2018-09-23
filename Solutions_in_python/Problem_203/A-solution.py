from Codejam import codejam_run
import copy

def linec(inp):
    R, C = inp.split(" ")
    return int(R)


@codejam_run(OFS="\n", I_line_count=linec)
def solve(RC, *args):
    R, C = (int(i) for i in RC)
    grid = list(args)
    grid = [list(l[0]) for l in grid]
    old_grid = copy.deepcopy(grid)


    #top down
    for row in range(1, R):
        for col in range(0, C):
            if grid[row][col] == '?':
                grid[row][col] = grid[row - 1][col]

    #bot up
    for row in reversed(range(0,R - 1)):
        for col in range(0, C):
            if grid[row][col] == '?':
                grid[row][col] = grid[row + 1][col]

    #left right
    for col in range(1, C):
        for row in range(0, R):
            if grid[row][col] == '?':
                grid[row][col] = grid[row][col - 1]

    #right left
    for col in reversed(range(0, C - 1)):
        for row in range(0, R):
            if grid[row][col] == '?':
                grid[row][col] = grid[row][col + 1]


    return ["".join(r) for r in grid]
