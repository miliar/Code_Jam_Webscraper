#! /usr/bin/env python
# watersheds.py (@DESC@)
# Maintainer: Matias Larre Borges <matias@larre-borges.com>

import sys
import string

MAX_HEIGHT = 10001
LETTERS = map(chr, range(97, 123))

class Cell:
    def __init__(self, x, y, height = MAX_HEIGHT):
        self.height = height
        self.label = '@'
        self.x = x
        self.y = y

    def __str__(self):
        return self.label

class Map:
    def __init__(self, lines, columns):
        self.lines = lines
        self.columns = columns
        self.label_counter = 0
        self.array = []
        for l in range(lines):
            for c in range(columns):
                self.array.append(Cell(l, c))

    def fill(self, lines):
        index = 0
        for line in lines:
            for height in line.split(' '):
                self.array[index].height = int(height)
                index += 1

    def free_label(self):
        label = LETTERS[self.label_counter]
        self.label_counter += 1
        return label

    def watershed(self, cell = None, path = None):
        index = 0
        while (index < (self.lines * self.columns)):
            cell = self.array[index]
            path = []
            if cell.label != '@':
                index += 1
                continue
            while True:
                if cell.label != '@':
                    break
                # Check neighbors
                # n = [ NORTH, WEST, EAST, SOUTH ]
                n = [Cell(-1, -1), Cell(-1, -1), Cell(-1, -1), Cell(-1, -1)]
                if cell.x > 0:                  # NORTH
                    n[0] = self.array[(cell.x - 1) * self.columns + cell.y]
                if cell.y > 0:                  # WEST
                    n[1] = self.array[cell.x * self.columns + (cell.y - 1)]
                if cell.y < (self.columns - 1): # EAST
                    n[2] = self.array[cell.x * self.columns + (cell.y + 1)]
                if cell.x < (self.lines - 1):   # SOUTH
                    n[3] = self.array[(cell.x + 1) * self.columns + cell.y]
                n.sort(lambda x, y: x.height - y.height)
                if n[0].height < cell.height:
                    path.append(cell)
                    cell = n[0]
                else:
                    # it's a sink
                    cell.label = self.free_label()
            for c in path:
                self.array[c.x * self.columns + c.y].label = cell.label
            self.array[cell.x * self.columns + cell.y].label = cell.label
            index += 1

    def __str__(self):
        result = ''
        c = 0
        for cell in self.array:
            result += str(cell)
            c += 1
            if c == self.columns:
                result += '\n'
                c = 0
            else:
                result += ' '
        return result


def main():
    file = open(sys.argv[1])

    nb_cases = int(file.readline())
    nb_case = 1
    for i in range(nb_cases):
        l, c = file.readline().split(' ')
        lines = int(l)
        columns = int(c)
        map = Map(lines, columns)
        map.fill([file.readline() for i in range(lines)])
        map.watershed()
        sys.stdout.write(("Case #%d:\n" % nb_case) + str(map))
        nb_case += 1

    file.close()

if __name__ == "__main__":
    main()
