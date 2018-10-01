#!/usr/bin/python

import sys
import string
import itertools

def read_int(file):
    return int(file.readline())

def read_int_array(file):
    return [int(i) for i in file.readline().split()]


class Cell():

    def __init__(self, map, index, row, col, value):
        self.map = map
        self.index = index
        self.row = row
        self.col = col
        self.value = value
        self.sources = []
        self.destination = None
        self.label = '?'

    def check(self):
        self.destination = self

        if self.row:
            self.check_neighbour(-1, 0)

        if self.col:
            self.check_neighbour(0, -1)

        if self.col < self.map.cols - 1:
            self.check_neighbour(0, 1)

        if self.row < self.map.rows - 1:
            self.check_neighbour(1, 0)

        if self.destination == self:
            self.destination = None

        else:
            self.destination.add_source(self)

    def check_neighbour(self, r, c):
        row = self.row + r
        col = self.col + c
        neighbour = self.map.at(row, col)
        if neighbour.value < self.destination.value:
            self.destination = neighbour

    def add_source(self, neighbour):
        self.sources.append(neighbour)

    def is_sink(self):
        return not self.destination

    def _direction(self):
        if not self.destination:
            return '.'

        if self.destination.row < self.row:
            return 'N'

        if self.destination.col < self.col:
            return 'W'

        if self.destination.col > self.col:
            return 'E'

        if self.destination.row > self.row:
            return 'S'

        return '?'


class Sink():

    def __init__(self, cell):
        self.cell = cell
        self.index = cell.index
        self.members = []

    def gather(self):
        queue = [self.cell]

        while queue:
            cell = queue.pop(0)

            if cell.index < self.index:
                self.index = cell.index

            self.members.append(cell)
            queue.extend(cell.sources)

    def mark(self, label):
        for member in self.members:
            member.label = label

class Map():

    def __init__(self, rows, cols, file):
        self.rows = rows
        self.cols = cols

        self.cells = []
        self.lookup = {}

        index = 0

        for row in xrange(rows):
            data = read_int_array(file)

            for col, value in enumerate(data):
                cell = Cell(self, index, row, col, value)
                index += 1
                self.cells.append(cell)
                self.lookup[row, col] = cell

        sinks = []

        for cell in self.cells:
            cell.check()
            if cell.is_sink():
                sinks.append(Sink(cell))

        for sink in sinks:
            sink.gather()

        sinks.sort(key=lambda s: s.index)

        for sink, label in itertools.izip(sinks, string.lowercase):
            sink.mark(label)

    def at(self, row, col):
        return self.lookup[row, col]

    def __str__(self):
        s = []

        i = iter(self.cells)
        for row in xrange(self.rows):
            s.append(' '.join(next(i).label for col in xrange(self.cols)))

        return '\n'.join(s)


def main():

    if len(sys.argv) < 2:
        print "need file"
        return

    with open(sys.argv[1]) as file:

        T = read_int(file)

        for n in xrange(T):

            H, W = read_int_array(file)
            map = Map(H, W, file)

            print "Case #{0}:".format(n + 1)
            print map



if __name__ == "__main__":
    main()

