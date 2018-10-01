'''
Created on 2009. 9. 3.

@author: Bang, Hyunsu
'''

def process(data):
    ret = list()
    cells = list()
    x = 0
    for i in data:
        ret.append([0]* len(i))
        y = 0
        for j in i:
            cells.append((x,y))
            y += 1
        x += 1
    res = list()
    num = 'a'
    while True:
#        print cells
#        print 'start', cells
        if len(cells) == 0:
            break
        direction = cells[0]
        footprint = list()
#        print 'roind)', footprint
        while (direction != 'x'):
#            print 'trying', direction
            x, y = direction
            footprint.append((x, y))
            direction = walk(data, *direction)
#            print ret
            if direction == 'x' or not str(ret[direction[0]][direction[1]]).isdigit():
#                print ret
                if direction == 'x':
                    ret[x][y] = num
                    num = chr(ord(num)+1)
                else:
#                    print data[x][y]
                    ret[x][y] = ret[direction[0]][direction[1]]
#                print 'low', x, y, footprint
#                print 'fp', footprint
                for c in footprint:
                    fx, fy = c
#                    print data[x][y]
                    ret[fx][fy] = ret[x][y]
#                    print cells, c, cells.index(c)
                    del cells[cells.index(c)]
                break
    return ret

def walk (data, x, y):
    if x == 0:
        north = 10001
    else:
        north = int(data[x - 1][y])
    if x == len(data) - 1:
        south = 10001
    else:
        south = int(data[x + 1][y])
    if y == 0:
        west = 10001
    else:
        west = int(data[x][y - 1])
    if y == len(data[x]) - 1:
        east = 10001
    else:
        east = int(data[x][y + 1])
    neighbor = [int(data[x][y]), north, west, east, south]
    low = min(neighbor)
    direction = neighbor.index(low)
    direction_list = ('x', (x-1, y), (x, y - 1), (x, y + 1), (x + 1,y))
    return direction_list[direction]

def main(input_fn):
    try:
        f = open(input_fn, 'r')
        o = open(input_fn+'.out', 'w')
    except IOError:
        print "Input file %s dos not exists" % (input_fn, )
        return 2
    
    lines = int(f.readline())
    
    for i in range(lines):
        rows, columns = f.readline().split()
#        print rows, columns
        matrix = list()
        for r in range(int(rows)):
            matrix.append(f.readline().split())
        ret = process(matrix)
#        print ret
        res = list()
        for ln in ret:
            res.append(' '.join(ln))
        print res
#        print matrix
        o.write('Case #' + str(i+1) + ':\n' + '\n'.join(res) + '\n')
    
import sys
if __name__ == '__main__':
    main(sys.argv[1])