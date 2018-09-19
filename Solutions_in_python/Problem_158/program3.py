import math
import copy

inp = open("in.txt")
out = open("out.txt", "w+")

def write_case(index, result):
    print result
    out.write("Case #%d: %s\n" % (index+1, result))

cases = int(inp.readline())  
block_cache = {
    1: [[[1]]]
}

def turn_block(b):
    turned = []
    for i in xrange(len(b[0])):
        row = []
        for j in xrange(len(b)-1, -1, -1):
            row.append(b[j][i])
        turned.append(row)
    return turned

def get_rotations(block):
    yield block
    for i in xrange(3):
        block = turn_block(block)
        yield block

def dedupe(s):
    seen = []
    for x in s:
        if x in seen:
            continue
        seen.append(x)
    return seen

def enumerate_polyominos(nsquares):
    if nsquares in block_cache:
        return block_cache[nsquares]
    result = dedupe(_enumerate_polyominos(nsquares))
    
    block_cache[nsquares] = result
    return result

def _enumerate_polyominos(nsquares):
    if nsquares == 1:
        yield [[1]]
        return
    
    for block in enumerate_polyominos(nsquares-1):
        for x in xrange(len(block)):
            for y in xrange(len(block[0])):
                if block[x][y] == 0:
                    b2 = copy.deepcopy(block)
                    b2[x][y] = 1
                    yield b2
            
            b2 = copy.deepcopy(block)
            b4 = copy.deepcopy(block)
            for x2 in xrange(len(block)):
                b2[x2] = [0] + b2[x2]
                b4[x2].append(0)
            
            if block[x][0] == 1:
                b3 = copy.deepcopy(b2)
                b3[x][0] = 1
                yield b3
            
            if block[x][-1] == 1:
                b3 = copy.deepcopy(b4)
                b3[x][-1] = 1
                yield b3
        
        for y in xrange(len(block[0])):
            b2 = copy.deepcopy(block)
            b4 = copy.deepcopy(block)
            b2 = [[0]*len(block[0])] + b2
            b4 = b4 + [[0]*len(block[0])]
            
            if block[0][y] == 1:
                b3 = copy.deepcopy(b2)
                b3[0][y] = 1
                yield b3
            
            if block[-1][y] == 1:
                b3 = copy.deepcopy(b4)
                b3[-1][y] = 1
                yield b3

def place_block(block, x, y, grid):
    if x + len(block) > len(grid):
        return None
    if y + len(block[0]) > len(grid[0]):
        return None
    
    g2 = copy.deepcopy(grid)
    
    for x2 in xrange(len(block)):
        for y2 in xrange(len(block[0])):
            if block[x2][y2] == 1:
                if grid[x+x2][y+y2] == 1:
                    return None
                g2[x+x2][y+y2] = 1
    return g2

def is_full(grid):
    for x in xrange(len(grid)):
        for y in xrange(len(grid[0])):
            if grid[x][y] == 0:
                return False
    return True

def hole_cells(grid, x, y):
    if grid[x][y] == 0:
        return []
    cells = [[x, y]]
    if len(grid) > (x+1):
        cells += hole_cells(grid, x+1, y)
    if len(grid[0]) > (y+1):
        cells += hole_cells(grid, x, y+1)
    return cells

def hole_too_small(grid, n):
    checked = []
    for x in xrange(len(grid)):
        for y in xrange(len(grid[0])):
            if grid[x][y] == 1 and [x, y] not in checked:
                cells = hole_cells(grid, x, y)
                if len(cells) < n:
                    return True
                checked += cells
    return False

def can_richard_win(block, r, c, ntomino, grid=None):
    if grid == None:        
        grid = []
        for i in xrange(r):
            grid.append([0]*c)
    
    for x in xrange(r):
        for y in xrange(c):
            grid2 = place_block(block, x, y, grid)
            
            if grid2 != None:
                if hole_too_small(grid2, ntomino):
                    continue
                if is_full(grid2):
                    return False
                for block2 in enumerate_polyominos(ntomino):
                    if can_richard_win(block2, r, c, ntomino, grid2) == False:
                        return False
    
    return True
    

def solve_case():
    x, r, c = [int(x) for x in inp.readline().split()]
    if (r*c) % x != 0:
        return "RICHARD"
    if x == 2:
        return "GABRIEL"
    
    for block in enumerate_polyominos(x):
        if all([can_richard_win(rotation, r, c, x) and can_richard_win(rotation, c, r, x) for rotation in get_rotations(block)]):
            print block
            return "RICHARD"
    return "GABRIEL"

print turn_block([[1, 1], [1, 0]])

for i in xrange(cases):
    print "case %s" % (i+1)
    write_case(i, solve_case())