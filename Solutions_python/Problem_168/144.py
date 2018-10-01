def solve():
    R,C = [int(x) for x in raw_input().split()]
    grid = [raw_input() for i in range(R)]
    
    cols = [len([grid[y][x] for y in range(R) if grid[y][x] != '.']) >= 2
            for x in range(C)]
    rows = [len([grid[y][x] for x in range(C) if grid[y][x] != '.']) >= 2
            for y in range(R)]

    for x in range(C):
        for y in range(R):
            if grid[y][x] != '.' and not (cols[x] or rows[y]):
                return "IMPOSSIBLE"
    
    out = 0
    for x in range(C):
        for y in range(R):
            if grid[y][x] == '^': out += 1
            if grid[y][x] != '.': break
        for y in reversed(range(R)):
            if grid[y][x] == 'v': out += 1
            if grid[y][x] != '.': break
    for y in range(R):
        for x in range(C):
            if grid[y][x] == '<': out += 1
            if grid[y][x] != '.': break
        for x in reversed(range(C)):
            if grid[y][x] == '>': out += 1
            if grid[y][x] != '.': break
    return out
            

for i in range(int(raw_input())):
    print "Case #%d: %s"%(i+1, solve())
