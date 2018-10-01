import sys

class Plane(object):
    def __init__(self, height, width, grid):
        self.height = height
        self.width = width
        self.grid = grid
    
    def at(self, x, y):
        if (x < 0 or x >= self.width or
            y < 0 or y >= self.height):
            return None
        else:
            return self.grid[y][x]
    
    def neighbors(self, cell):
        return [cell for cell in
                [
                 plane.at(cell.x, cell.y - 1), #n
                 plane.at(cell.x - 1, cell.y), #w
                 plane.at(cell.x + 1, cell.y), #e
                 plane.at(cell.x, cell.y + 1)  #s
                ] if cell]
        
    def print_plane(self, field):
        for y in range(height):
            for x in range(width):
                cell = plane.at(x, y)
                sys.stdout.write(str(getattr(cell, field)) + " ")
            sys.stdout.write("\n")
            
    def print_plane2(self, field, field2):
        for y in range(height):
            for x in range(width):
                cell = plane.at(x, y)
                sys.stdout.write(str(getattr(getattr(cell, field), field2)) + " ")
            sys.stdout.write("\n")

class Cell(object):
    def __init__(self, x, y, altitude):
        self.x = x
        self.y = y
        self.altitude = altitude
        self.water = 1
        self.sink_for = [self]
        self.sink = self
        self.label = None
        
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + "," + str(self.altitude) + ")"
    
    def drain_to(self, neighbor):
        # move the water
        my_water = self.water
        neighbor.water += my_water
        self.water -= my_water
        
        # now track the sink
        neighbor.sink_for = neighbor.sink_for + self.sink_for
        for cell in neighbor.sink_for:
            cell.sink = neighbor
        self.sink_for = []
        
        return my_water != self.water
    

test_cases = int(sys.stdin.readline().strip())
for test_case in range(test_cases):
    height, width = map(int, sys.stdin.readline().strip().split(" "))
    
    grid = []
    for y in range(height):
        row = []
        for x, alt in enumerate(map(int, sys.stdin.readline().strip().split(" "))):
            row.append(Cell(x, y, alt))
        grid.append(row)
    
    plane = Plane(height, width, grid)
    
    while True:
        drained_this_time = False
        for y in range(height):
            for x in range(width):
                cell = plane.at(x, y)
                
                neighbors = plane.neighbors(cell)
                lowest_neighbor = cell
                for neighbor in neighbors:
                    if neighbor.altitude < lowest_neighbor.altitude:
                        lowest_neighbor = neighbor
                
                drained_this_time = drained_this_time or cell.drain_to(lowest_neighbor)

        if not drained_this_time:
            break
        
    labels = "abcdefghijklmnopqrstuvwxyz"
    label_i = 0
    for y in range(height):
        for x in range(width):
            cell = plane.at(x, y)
            
            if not cell.sink.label:
                cell.sink.label = labels[label_i]
                label_i += 1

    print "Case #" + str(test_case + 1) + ":"
    plane.print_plane2("sink", "label")