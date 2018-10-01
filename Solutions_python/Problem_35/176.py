def main(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    outlines = []
    
    NORTH, WEST, EAST, SOUTH = 0, 1, 2, 3
    
    T = int(lines.pop(0))
    
    def get_neighbours(arr, row, col):
        neighbours = []
        if row > 0:
            neighbours.append((NORTH, arr[row - 1][col]))
        if col > 0:
            neighbours.append((WEST, arr[row][col - 1]))
        if col < W - 1:
            neighbours.append((EAST, arr[row][col + 1]))
        if row < H - 1:
            neighbours.append((SOUTH, arr[row + 1][col]))
        return neighbours
    
    for case in xrange(T):
        H, W = map(lambda x:int(x), lines.pop(0).split(' '))
        alt_map = []
        link_map = []
        basin_map = []
        
        for i in xrange(H):
            alt_map.append(map(lambda x:int(x), lines.pop(0).split(' ')))
        
        for row in xrange(H):
            link_map.append([])
            for col in xrange(W):
                neighbours = get_neighbours(alt_map, row, col)
                if len(neighbours) > 0:
                    min_alt = min(zip(*neighbours)[1])
                    if min_alt < alt_map[row][col]:
                        flow_to = filter(lambda x:x[1] == min_alt, neighbours)
                        tgt_cell = flow_to[0]
                        if len(flow_to) > 1:
                            min_dir = min(zip(*flow_to)[0])
                            tgt_cell = filter(lambda x: x[0] == min_dir, flow_to)[0]
                        link_map[row].append(tgt_cell[0])
                    else:
                        link_map[row].append(-1)
                else:
                    link_map[row].append(-1)
                    
        def get_delta_row_col(dir):
            delta_row = 0
            delta_col = 0
            if dir == NORTH:
                delta_row = -1
            elif dir == WEST:
                delta_col = -1
            elif dir == EAST:
                delta_col = 1
            elif dir == SOUTH:
                delta_row = 1
            return (delta_row, delta_col)
        
        def get_conn(row, col):
            connected = []
            cur_dir = link_map[row][col]
            if cur_dir != -1:
                d_row, d_col = get_delta_row_col(cur_dir)
                connected.append((row + d_row, col + d_col))
                link_map[row][col] = -1
            
            neighbours = get_neighbours(link_map, row, col)
            for dir, link_dir in neighbours:
                if (3 - dir) == link_dir:
                    d_row, d_col = get_delta_row_col(dir)
                    connected.append((row + d_row, col + d_col))
                    link_map[row + d_row][col + d_col] = -1
            
            return connected
            
        basin_map = list(alt_map)
        cur_char = 'a'
        nodes = []
        num_accounted = 0
        i = 0
        j = 0
        while num_accounted < H * W:
            while True:
                if isinstance(basin_map[i][j], int):
                    nodes.append((i, j))
                    break
                j += 1
                if j == W:
                    j = 0
                    i += 1
            
            while len(nodes) > 0:
                node_row, node_col = nodes.pop(0)
                basin_map[node_row][node_col] = cur_char
                num_accounted += 1
                
                for row, col in get_conn(node_row, node_col):
                    nodes.append((row, col))
                
            cur_char = chr(ord(cur_char) + 1)
        
        line = 'Case #%i:\n' % ((case + 1))
        for row in xrange(H):
            line += ' '.join(basin_map[row])
            line += '\n'
        outlines.append(line)
    
    f = open('B.out', 'w')
    f.writelines(outlines)
    f.close()

if __name__ == "__main__":
    main('B-large.in')