from sys import stdin, stdout
from copy import deepcopy

def propagate(element, r, c, R, C, grid):
    applied = ({r})
    for _r in range(r - 1, -1, -1):
        if grid[_r][c] == "?":
            grid[_r][c] = element
            applied.add(_r)

        else:
            break

    for _r in range(r + 1, R):
        if grid[_r][c] == "?":
            grid[_r][c] = element
            applied.add(_r)

        else:
            break

    for _c in range(c - 1, -1, -1):
        if all(grid[_r][_c] == "?" for _r in applied):
            for _r in applied:
                grid[_r][_c] = element

        else:
            break

    for _c in range(c + 1, C):
        if all(grid[_r][_c] == "?" for _r in applied):
            for _r in applied:
                grid[_r][_c] = element
        else:
            break

def propagate_2(element, r, c, R, C, grid):
    applied = ({c})
    for _c in range(c - 1, -1, -1):
        if grid[r][_c] == "?":
            grid[r][_c] = element
            applied.add(_c)

        else:
            break

    for _c in range(c + 1, C):
        if grid[r][_c] == "?":
            grid[r][_c] = element
            applied.add(_c)

        else:
            break

    for _r in range(r - 1, -1, -1):
        if all(grid[_r][_c] == "?" for _c in applied):
            for _c in applied:
                grid[_r][_c] = element

        else:
            break

    for _r in range(r + 1, R):
        if all(grid[_r][_c] == "?" for _c in applied):
            for _c in applied:
                grid[_r][_c] = element
        else:
            break

def get_grid_str(grid):
    return"\n"+ "\n".join("".join(row) for row in grid)

def solve(R, C, grid):
    original_grid = deepcopy(grid)

    for prop_fn in [propagate, propagate_2]:
        completed = set()
        for r in range(R):
            for c in range(C):
                if grid[r][c] != "?" and grid[r][c] not in completed:
                    prop_fn(grid[r][c], r, c, R, C, grid)
                    completed.add(grid[r][c])

        if "?" not in get_grid_str(grid):
            break
        else:
            grid = original_grid

    return get_grid_str(grid)



T = int(stdin.readline())

for t in range(T):
    R, C = map(int, stdin.readline().strip().split())

    grid = []
    for _ in range(R):
        grid.append(list(stdin.readline().strip()))

    result = solve(R, C, grid)

    stdout.write("Case #{}: {}\n".format(t+1, result))