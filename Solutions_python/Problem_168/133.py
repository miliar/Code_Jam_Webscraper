import sys

DIRS = {
    '^': (0, -1),
    'v': (0, 1),
    '<': (-1, 0),
    '>': (1, 0)
}

def in_bounds(grid, x, y):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

def is_ending(grid, x, y, dc):
    dx = DIRS[dc]
    x += dx[0]
    y += dx[1]
    while in_bounds(grid, x, y):
        if grid[y][x] != '.':
            return True
        x += dx[0]
        y += dx[1]

    return False

def solve(f):
    r, c = map(int, f.readline().split())
    grid = []
    for _ in xrange(r):
        grid.append(f.readline().rstrip())

    changes = 0
    for y in xrange(r):
        for x in xrange(c):
            if grid[y][x] != '.':
                if not is_ending(grid, x, y, grid[y][x]):
                    possible = False
                    for d in DIRS.keys():
                        if is_ending(grid, x, y, d):
                            possible = True
                            changes += 1
                            break
                    if not possible:
                        return "IMPOSSIBLE"
    return changes


def solve_all(f, o):
    t = int(f.readline())
    for c in xrange(t):
        o.write("Case #{}: {}\n".format(c + 1, solve(f)))


def main():
    if len(sys.argv) < 2:
        solve_all(sys.stdin, sys.stdout)
    else:
        in_f = "./in/{}.in".format(sys.argv[1])
        out_f = "./out/{}.out".format(sys.argv[1])
        with open(in_f) as f, open(out_f, "w") as o:
            solve_all(f, o)

main()