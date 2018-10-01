
import copy
from functools import *


def mk_grid(rows, cols):
    res = []
    res.append(['+']*(cols+2))
    for _ in range(rows):
        res.append(['.']*(cols+2))
        res[-1][0] = res[-1][-1] = '+'
    res.append(['+']*(cols+2))
    return res

def toString(grid):
    s = ''
    for r in grid:
        s += ''.join(r)
    return s

def print_grid(grid):
    for r in grid:
        print(''.join(r))


def environment(grid, y, x):
    global R, C
    return [ (y+oy, x+ox) for (oy, ox) in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]]


def is_null_cell(grid, y, x):
#    return grid[y][x] == '.' and all([grid[e[0]][e[1]]!='*'  for e in environment(grid, y, x)])
    if grid[y][x] == '*':
        return False
    else:
        U = environment(grid, y, x)
        a = [grid[e[0]][e[1]]!='*' for e in U]
        f = all(a)
        return f

def mark_reachable_cells(grid, y, x):
    grid[y][x] = '#'
    if is_null_cell(grid, y, x):
        grid[y][x] = 'N'
        for o in environment(grid, y, x):
            if grid[o[0]][o[1]] == '.': mark_reachable_cells(grid, o[0], o[1])

def all_reachable(grid):
    for row in grid:
        if '.' in row:
            return False
    return True

def is_solution(grid):
    global R, C
    candidates = []
    for r, row in enumerate(grid):
        for c, x in enumerate(row):
            if x == '.':
                candidates.append((r,c))

    for c in candidates:
        g1 = copy.deepcopy(grid)
        mark_reachable_cells(g1, c[0], c[1])
        if all_reachable(g1):
            # print_grid(g1)
            return True, c
    return False, None

def fill_heuristic(grid, bombs):
    """
        fill complete rows or columns
        return number of unplaced bombs
    """

    global R, C
    y, x = 0, 0
    while bombs > 0:
        if (bombs >= C-x) and (R-y >= C-x):
            for xx in range(x, C):
                grid[y+1][xx+1] = '*'
                bombs -= 1
                if bombs == 0: break
            y += 1
        elif (bombs >= R-y) and (C-x > R-y):
            for yy in range(y, R):
                grid[yy+1][x+1] = '*'
                bombs -= 1
                if bombs == 0: break
            x += 1
        else:
            break

    return bombs


def fill_grid(grid, bombs):
    global R, C, cache
    candidates = []
    for r, row in enumerate(grid):
        for c, x in enumerate(row):
            if x == '.':
                candidates.append((r,c))

    found = False
    if bombs == 0:
        f, start = is_solution(copy.deepcopy(grid))
        if f:
            grid[start[0]][start[1]] = 'c'
            found = True
        return found

    for c in candidates:
            grid[c[0]][c[1]] = '*'
            if bombs>1:
                found = fill_grid(grid, bombs-1)
            else:
                k = toString(grid)
                if k in cache:
                    (f, start) = cache[k]
                else:
                    f, start = is_solution(copy.deepcopy(grid))
                    cache[k] = (f, start)
                if f:
                    grid[start[0]][start[1]] = 'c'
                    found = True
            if found:
                break
            grid[c[0]][c[1]] = '.'

    return found


f = open(r"e:\downloads\C-small-attempt3.in", "r")
#f = open(r"e:\downloads\minesweeper_master.txt", "r")

T = int(f.readline())
for t in range(1, T+1):
    R, C, M = map(int, f.readline().split())

    # print R, C, M
    grid = mk_grid(R, C)
    cache = {}
    M = fill_heuristic(grid, M)
    found = fill_grid(grid, M)

    s = ''
    for row in grid[1:-1]:
        s += ''.join(row[1:-1])+"\n"

    if found:
        print("Case #%d:\n%s" % (t, s))
    else:
        print("Case #%d:\nImpossible" % t)


