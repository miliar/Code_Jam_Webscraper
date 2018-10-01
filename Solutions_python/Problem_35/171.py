
MAX_ALT = 10000

NORTH = "NORTH"
SOUTH = "SOUTH"
EAST = "EAST"
WEST = "WEST"
SINK = "SINK"

class Grid(object):
    def __init__(self, w, h, values=None):
        self.w = w
        self.h = h
        if values is None:
            values = [[None for i in xrange(w)] for j in xrange(h)]
        self.values = values
    def get(self, row, col):
        if row<0 or row>=self.h or col<0 or col>=self.w:
            return MAX_ALT
        else:
            return self.values[row][col]
    def set(self, row, col, v):
        self.values[row][col] = v
    def __repr__(self):
        return "\n".join(" ".join(str(i) for i in rowvalues) for rowvalues in self.values)

def calc_flow(w, h, grid):
    flow_grid = Grid(w,h)
    for row in xrange(h):
        for col in xrange(w):
            alts = {}
            alts[SINK] = grid.get(row, col)
            alts[WEST] = grid.get(row, col-1)
            alts[EAST] = grid.get(row, col+1)
            alts[NORTH] = grid.get(row-1, col)
            alts[SOUTH] = grid.get(row+1, col)
            flow_grid.set(
                row, col,
                list(sorted(
                    (SINK,NORTH,WEST,EAST,SOUTH),
                    key=lambda d:alts[d]))[0])
    return flow_grid

ALPHA = "abcdefghijklmnopqrstuvwxyz"

def calc_arbitrary_basins(w, h, flow_grid):
    basin_grid = Grid(w,h)
    next_sink = 0
    for row in xrange(h):
        for col in xrange(w):
            basin = basin_grid.get(row, col)
            if basin is not None:
                continue
            walkrow = row
            walkcol = col
            walk=[]
            sinkletter=None
            while True:
                walk.append((walkrow, walkcol))
                direction = flow_grid.get(walkrow, walkcol)
                if direction==SINK:
                    sinkletter = ALPHA[next_sink]
                    next_sink += 1
                elif direction==NORTH:
                    walkrow -= 1
                elif direction==SOUTH:
                    walkrow += 1
                elif direction==WEST:
                    walkcol -= 1
                elif direction==EAST:
                    walkcol += 1
                basin = basin_grid.get(walkrow, walkcol)
                if basin is not None:
                    sinkletter = basin
                if sinkletter is not None:
                    for (markrow, markcol) in walk:
                        basin_grid.set(markrow, markcol, sinkletter)
                    break
    return basin_grid

def sort_basins(grid):
    w = grid.w
    h = grid.h
    seenbasins = []
    basinindices = []
    index = 0
    
    for row in xrange(h):
        for col in xrange(w):
            basin = basin_grid.get(row, col)
            if basin not in seenbasins:
                seenbasins.append(basin)
                basinindices.append((basin,index))
                index+=1

    basinindices.sort()
    mapping = {}
    for newindex, (basinname, oldindex) in enumerate(basinindices):
        mapping[ALPHA[oldindex]] = ALPHA[newindex]

    sorted_grid = Grid(w,h)
    
    for row in xrange(h):
        for col in xrange(w):
            sorted_grid.set(row, col, mapping[grid.get(row, col)])
    
    return sorted_grid

def read_grid():
    h, w = (int(s) for s in raw_input().strip().split(" "))
    gridvalues = []
    for row in xrange(h):
        rowvalues = [int(s) for s in raw_input().strip().split(" ")]
        gridvalues.append(rowvalues)
    return Grid(w, h, gridvalues)

numcases = int(raw_input().strip())
for i in xrange(numcases):
    print "Case #{0}:".format(i+1)
    grid = read_grid()
    flow_grid = calc_flow(grid.w, grid.h, grid)
    basin_grid = calc_arbitrary_basins(grid.w, grid.h, flow_grid)
    sorted_grid = sort_basins(basin_grid)
    print sorted_grid
