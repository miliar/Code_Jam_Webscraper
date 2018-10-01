from sys import argv, stdout
from pprint import pprint
from copy import deepcopy

def reflectOminoSide(side):
    if side == 0:
        return 0
    elif side == 1:
        return 3
    elif side == 2:
        return 2
    elif side == 3:
        return 1

def oppositeOminoSide(side):
    if side == 0:
        return 2
    elif side == 1:
        return 3
    elif side == 2:
        return 0
    elif side == 3:
        return 1


def rotateOminoSide(side, mag):
    return (side + mag) % 4

def translateCoord(coord, dir, orient, mag=1):
    if orient.reflect:
        dir = reflectOminoSide(dir)
    dir = rotateOminoSide(dir,orient.rotate)

    if dir == 0:
        return (coord[0], coord[1] - mag)
    elif dir == 1:
        return (coord[0] + mag, coord[1])
    elif dir == 2:
        return (coord[0], coord[1] + mag)
    elif dir == 3:
        return (coord[0] - mag, coord[1])

class Orient:
    def __init__(self, reflect = False, rotate = 0):
        self.reflect = reflect
        self.rotate = rotate


class Omino:
    def __init__(self):
        self.sides = [None,None,None,None]
        self.mark = False

    def attach(self,side,omino=None):
        if omino == None:
            omino = Omino()
        self.sides[side] = omino
        omino.sides[oppositeOminoSide(side)] = self
        return omino

class Cell:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.group = None
        self.val = val

    def __hash__(self):
        return (self.x,self.y).__hash__()

    def __cmp__(self, other):
        if self.x == other.x:
            return self.y - other.y
        else:
            return self.x - other.x

    def __str__(self):
        return '(%d,%d)' % (self.x, self.y)

    def __repr__(self):
        return self.__str__()

def createFours():
    results = []
    
    # Square
    omino = Omino()
    omino.attach(1).attach(2).attach(3).attach(0, omino)
    results.append(omino)

    # L
    omino = Omino()
    omino.attach(3).attach(2).attach(2)
    results.append(omino)

    # Tack
    omino = Omino()
    omino.attach(0)
    omino.attach(2)
    omino.attach(3)
    results.append(omino)

    # Squiggle
    omino = Omino()
    omino.attach(2).attach(1).attach(2)
    results.append(omino)

    # Line
    results.append(Omino().attach(2).attach(2).attach(2))

    return results

ones = [Omino()]
twos = [Omino().attach(0)]
threes = [Omino().attach(0).attach(0),
    Omino().attach(2).attach(1)]
fours = createFours()
all_ominos = ['',ones,twos,threes,fours]

sample_grid_1 = [[True,True,True,True],
    [True,False,False,True],
    [True,False,False,True],
    [True,True,True,True]]

sample_grid_2 = [
[True,False,True,False],
[True,False,True,False],
[True,False,True,False],
[True,False,True,False]
]

sample_grid_3 = [[False,False],
[False,False]]

sample_grid_4 = [
[False,False,False,False],
[False,False,False,False],
[False,False,False,False],
[False,False,False,False]
]

def clearOmino(omino):
    def clearOminoHelper(omino, visited):
        if omino in visited:
            return
        visited.append(omino)
        omino.mark = False
        for side in omino.sides:
            if side != None:
                clearOminoHelper(side, visited)
    visited = []
    clearOminoHelper(omino, visited)


def get_omino_line(omino,orient):
    def get_omino_line_helper(omino, coord, coords):
        if omino.mark:
            return
        omino.mark = True
        coords.append(coord)
        for i, side in enumerate(omino.sides):
            if side != None:
                get_omino_line_helper(side, translateCoord(coord, i, orient), coords)


    clearOmino(omino)
    coords = []
    get_omino_line_helper(omino, (0,0), coords)
    return coords

def translate_line(line, x, y):
    return [(c[0] + x,c[1] + y) for c in line]

def print_grid(grid):
    output = ''
    for row in grid:
        for col in row:
            output += ('X' if col else '.')
        output += '\n'
    print output


def print_omino(omino, orient = Orient()):
    coords = get_omino_line(omino,orient)
    x = 0
    y = 0
    for c in coords:
        if c[0] < x:
            x = c[0]
        if c[1] < y:
            y = c[1]
    coords = [(c[0] - x, c[1] - y) for c in coords]
    # print coords
    x = 0
    y = 0
    for c in coords:
        if c[0] > x:
            x = c[0]
        if c[1] > y:
            y = c[1]
    # print 'X %d Y %d' % (x,y)
    grid = [[False for j in range(y + 1)] for i in range(x + 1)]
    # print 'X %d Y %d' % (len(grid),len(grid[0]))
    for c in coords:
        grid[c[0]][c[1]] = True

    print_grid(grid)

def gather_cells(omino):
    clearOmino(omino)
    cells = []
    def gather_cells_helper(omino):
        if omino == None or omino.mark:
            return
        omino.mark = True
        cells.append(omino)
        for side in omino.sides:
            gather_cells_helper(side)
    gather_cells_helper(omino)
    return cells

def place_line(line, grid):
    new_grid = deepcopy(grid)
    for p in line:
        if (p[0] >= 0 and p[0] < len(grid) and p[1] >= 0 and p[1] < len(grid[0])) and not new_grid[p[0]][p[1]]:
            new_grid[p[0]][p[1]] = True
        else:
            return
    return new_grid

def create_grid(r,c):
    return [[False for j in range(c)] for i in range(r)]

def check_grid(grid):
    for row in grid:
        for col in row:
            if not col:
                return False
    return True

def cellify(grid):
    return [[Cell(i, j, col) for j, col in enumerate(row)] for i, row in enumerate(grid)]

def groupify(grid):
    # print_grid(grid)
    grid = cellify(grid)
    groups = []

    def check_bounds(x, y):
        return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])

    def associate(ac, bc):
        # print '=' * 10
        # print groups
        # print ac
        # print ac.group
        # print bc
        # print bc.group
        if ac.group != None and bc.group != None:
            # print groups
            # print '%s\n%s' % (str(ac.group), str(bc.group))
            # merge groups
            # print groups
            groups.remove(ac.group)
            groups.remove(bc.group)
            new_group = ac.group.union(bc.group)
            for c in ac.group:
                c.group = new_group
            for c in bc.group:
                c.group = new_group
            # bc.group = ac.group
            groups.append(new_group)
        # elif ac.group == None and bc.group == None:
        #     g = set([ac, bc])
        #     ac.group = g
        #     bc.group = g
        #     groups.append(g)
        else:
            g = ac.group if ac.group != None else bc.group
            nong = ac if ac.group == None else bc
            nong.group = g
            g.add(nong)

    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            current = grid[i][j]
            if current.group == None:
                g = set([current])
                groups.append(g)
                current.group = g
            for offset in [(0,-1), (0,1), (-1,0), (1,0)]:
                check_x = i + offset[0]
                check_y = j + offset[1]
                if check_bounds(check_x, check_y):
                    sample = grid[check_x][check_y]
                    if current.val == sample.val and current.group != sample.group:
                        associate(current, sample)
    return [list(g) for g in groups]

def any_gaps(groups, x):
    for group in groups:
        if len(group) < x:
            return True
    return False

def fill_perfect_holes(grid, groups, x):
    for group in groups:
        if len(group) == x:
            for p in group:
                grid[p.x][p.y] = True

def main():
    input_file = argv[1]
    output_file = argv[2]

    with open(input_file,'r') as fin:
        # with stdout as fout:
        with open(output_file,'w') as fout:
            num = int(fin.readline().strip())
            testcase = 1
            for line in fin:
                if line[0] == '#':
                    continue
                print 'Testcase %d' % testcase
                line = line.strip()
                splits = line.split(' ')
                x = int(splits[0])
                r = int(splits[1])
                c = int(splits[2])
                
                success = False
                if x == 1:
                    success = True
                elif (r * c) % x == 0:
                    specific_ominos = list(all_ominos[x])
                    specific_ominos = [gather_cells(omino) for omino in all_ominos[x]]
                    success = True
                    for cells in specific_ominos:
                        # print '=' * 50
                        # print 'Omino'
                        # print cells
                        # print_omino(cells[0])
                        def solve(given_cells, grid, use_given):
                            if check_grid(grid):
                                return True
                            # print '*' * 40
                            # print_grid(grid)
                            orient = Orient()
                            for cells in ([given_cells] if use_given else specific_ominos):
                                for grid_x in range(len(grid)):
                                    for grid_y in range(len(grid[0])):
                                        if grid[grid_x][grid_y]:
                                            continue
                                        for cell in cells:
                                            for reflection in [False, True]:
                                                for rotation in [0,1,2,3]:
                                                    orient.reflect = reflection
                                                    orient.rotate = rotation
                                                    line = get_omino_line(cell, orient)
                                                    line = translate_line(line, grid_x, grid_y)
                                                    new_grid = place_line(line, grid)
                                                    if new_grid != None:
                                                        groups = groupify(new_grid)
                                                        if not any_gaps(groups, x):
                                                            fill_perfect_holes(new_grid, groups, x)
                                                            result = solve(None, new_grid, False)
                                                            if result:
                                                                return True
                            return False
                        result = solve(cells,create_grid(r,c), True)
                        if not result:
                            success = False
                            break
                result = 'GABRIEL' if success else 'RICHARD'
                fout.write('Case #%d: %s\n' % (testcase, result))
                testcase += 1

def test():
    # a = groupify(sample_grid_1)
    # print a
    # print '*' * 20
    # print set(a[0]).intersection(set(a[1]))
    # print '*' * 20

    # b = groupify(sample_grid_2)
    # print b
    print groupify(sample_grid_4)


if __name__ == '__main__':
    # test()
    main()



