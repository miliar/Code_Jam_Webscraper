import numpy

def process(filename):
    in_file = open(filename)

    T = int(in_file.readline().strip())
    for test_num in range(T):
        H, W = map(int, in_file.readline().strip().split())

        altitudes = numpy.zeros((H, W), 'i')
        result = numpy.zeros((H, W), 'i')

        for j in range(H):
            altitudes[j] = map(numpy.int32, in_file.readline().strip().split())

        current_basin = ord('a')

        def process_cell(cell):
            current_path.append(cell)
            neighbors = []
            if cell[0] - 1 >= 0:
                neighbors.append((cell[0] - 1, cell[1]))
            if cell[1] - 1 >= 0:
                neighbors.append((cell[0], cell[1] - 1))
            if cell[1] + 1 < W:
                neighbors.append((cell[0], cell[1] + 1))
            if cell[0] + 1 < H:
                neighbors.append((cell[0] + 1, cell[1]))

            min_altitude = 20000
            min_neighbor = None
            for neighbor in neighbors:
                neighbor_altitude = altitudes[neighbor]
                if neighbor_altitude < min_altitude:
                    min_altitude = neighbor_altitude
                    min_neighbor = neighbor
            if min_altitude < altitudes[cell]:
                process_cell(min_neighbor)
            
        
        while True:
            current = None
            found = False
            for i in range(H):
                if found:
                    break
                for j in range(W):
                    if found:
                        break
                    if result[i, j] == 0:
                        current = (i, j)
                        found = True
            if not found:
                break
            current_path = []
            process_cell(current)
            if result[current_path[-1]] != 0:
                for node in current_path:
                    result[node] = result[current_path[-1]]
            else:
                for node in current_path:
                    result[node] = current_basin
                current_basin += 1
        print 'Case #%d:' % (test_num+1)
        for row in result:
            print ' '.join(map(chr, row))
        

    
if __name__ == '__main__':
    import sys
    process(sys.argv[1])
