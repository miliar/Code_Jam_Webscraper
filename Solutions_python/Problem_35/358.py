import sys

SINK = 0
NORTH = 1
WEST = 2
EAST = 3
SOUTH = 4

flowletters = {
    SINK: '?',
    NORTH: 'N',
    WEST: 'W',
    EAST: 'E',
    SOUTH: 'S',
}

def get_flow_for_point(map, H, W, x, y):
    maxdiff = 0
    result = SINK
    height = map[y][x]
    if y < H-1:
        nheight = map[y+1][x]
        if nheight < height and height-maxdiff >= nheight:
            maxdiff = height - nheight;
            result = SOUTH
    if x < W-1:
        nheight = map[y][x+1]
        if nheight < height and height-maxdiff >= nheight:
            maxdiff = height - nheight;
            result = EAST
    if x > 0:
        nheight = map[y][x-1]
        if nheight < height and height-maxdiff >= nheight:
            maxdiff = height - nheight;
            result = WEST
    if y > 0:
        nheight = map[y-1][x]
        if nheight < height and height-maxdiff >= nheight:
            maxdiff = height - nheight;
            result = NORTH
    return result


def generate_flow_map(map, H, W):
    return [[get_flow_for_point(map, H, W, x, y) for x in range(W)] for y in range(H)]
    
def print_flow_map(map):
    for row in map:
        print " ".join([flowletters[val] for val in row])

def find_sink(flow_map, H, W, x, y):
    while(flow_map[y][x] != SINK):
        flow = flow_map[y][x]
        if flow == NORTH:
            y -= 1
        elif flow == EAST:
            x += 1
        elif flow == SOUTH:
            y += 1
        elif flow == WEST:
            x -= 1
    return x, y


def mark_basin(basin_map, flow_map, H, W, sx, sy, label):
    queue = [(sx, sy)]
    while len(queue) > 0:
        x, y = queue[0]
        queue = queue[1:]
        basin_map[y][x] = label
        if y < H-1 and basin_map[y+1][x] == None and flow_map[y+1][x] == NORTH:
            queue.append((x, y+1))
        if x < W-1 and basin_map[y][x+1] == None and flow_map[y][x+1] == WEST:
            queue.append((x+1, y))
        if x > 0 and basin_map[y][x-1] == None and flow_map[y][x-1] == EAST:
            queue.append((x-1, y))
        if y > 0 and basin_map[y-1][x] == None and flow_map[y-1][x] == SOUTH:
            queue.append((x, y-1))
    
def generate_basin_map(flow_map, H, W):
    basin_map = [[None for x in range(W)] for y in range(H)]
    basin_num = 0
    for y in range(H):
        for x in range(W):
            if basin_map[y][x] == None:
                sx, sy = find_sink(flow_map, H, W, x, y)
                mark_basin(basin_map, flow_map, H, W, sx, sy, chr(ord('a')+basin_num))
                basin_num += 1
    return basin_map
                
def solve_map(num):
    print "Case #%i:" % num
    dims = sys.stdin.readline().strip().split(' ')
    H, W = int(dims[0]), int(dims[1])
    def parse_map_line(width):
        return [int(val) for val in sys.stdin.readline().strip().split(' ')]
    map = [parse_map_line(W) for y in xrange(H)]
    flowmap = generate_flow_map(map, H, W)
    basin_map = generate_basin_map(flowmap, H, W)
    for row in basin_map:
        print " ".join(row)


if __name__=='__main__':
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        solve_map(t+1)
