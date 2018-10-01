#!/usr/bin/env python

import sys

class Basin(object):
    def __init__(self, level):
        self.label = None
        self.sink = False
        self.level = int(level)


class Maps(object):
    def __init__(self, config_file):
        self.maps = self.parse(config_file)

    def parse(self, config_file):
        fp = open(config_file)
        lines = fp.readlines()
        fp.close()
        grids = int(lines.pop(0))

        map = []

        for grid in range(grids):
            width = lines.pop(0).split(' ')[0]
            width = int(width)
            for i in range(width):
                map.append([])
                line = lines.pop(0)
                for item in line.split(' '):
                    map[i].append(Basin(item))

            yield map
            map = []

    def getNeighbours(self, map, i, j):
        if i != 0:
            north = (map[i-1][j].level, i-1, j)
        else:
            north = None

        if j != 0:
            west = (map[i][j-1].level, i, j-1)
        else:
            west = None

        if j != len(map[i]) - 1:
            east = (map[i][j+1].level, i, j+1)
        else:
            east = None

        if i != len(map) - 1:
            south = (map[i+1][j].level, i+1, j)
        else:
            south = None

        return (north, west, east, south)

    def getLower(self, neighbours, level):
        lower = None
        for neighbour in neighbours:
            if neighbour:
                if lower == None:
                    lower = neighbour
                else:
                    if neighbour[0] < lower[0]:
                        lower = neighbour


        if lower and lower[0] < level:
            return (lower[1], lower[2])
        else:
            return None


    def flowsTo(self, map, i, j):
        neighbours = self.getNeighbours(map, i, j)
        lower = self.getLower(neighbours, map[i][j].level)

        return lower


    def rain(self, labels, i, j, map):
        if map[i][j].sink or map[i][j].label:
            if not map[i][j].label:
                map[i][j].label = labels.pop(0)

        else:
            next = self.flowsTo(map, i, j)
            if not next:
                map[i][j].sink = True
                map[i][j].label = labels.pop(0)
            else:
                map[i][j].label = self.rain(labels, next[0], next[1], map)

        return map[i][j].label

    def run(self):
        output = open('output.out', 'w')
        case = 1
        for m in self.maps:
            labels = map(chr, range(97, 123))
            for i in range(len(m)):
                for j in range(len(m[i])):
                    if not m[i][j].label:
                        m[i][j].label = self.rain(labels, i, j, m)


            output.write('Case #%d:\n' % case)
            case += 1
            for line in m:
                for item in line:
                    output.write('%c ' % item.label)
                output.write('\n')
        output.close()



def main(argv):
    if len(argv) != 2:
        sys.stderr.write("USE: %s <input file>" % argv[0])
        return 1

    maps = Maps(argv[1])
    maps.run()

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
