#!/usr/bin/python3
#
# NOTE: will not work in Python 2.x
#

import sys

class Node:
    errorlabel = '***ERROR***'
    maxalt = sys.maxsize

    def __init__(self, altitude, label=None):
        self.altitude = altitude
        self.label = label

    @classmethod
    def make_error_node(cls):
        return cls(cls.maxalt, cls.errorlabel)

    def __repr__(self):
        return 'Node({!r}, {!r})'.format(self.altitude, self.label)

    def set_label(label):
        self.label = label

    def valid(self):
        return self.label != self.errorlabel

    def render(self, altitude=True, label=True):
        if self.label:
            printlabel = self.label
        else:
            printlabel = '_'

        if altitude and label:
            return '{}|{}'.format(self.altitude, printlabel)
        elif altitude:
            return str(self.altitude)
        elif label:
            return str(printlabel)

class DrainageMap:
    OutOfBounds = Node.make_error_node()

    @classmethod
    def readmap(cls, height, width):
        """
        Return a new map read from stdin.
        """
        dmap = DrainageMap()
        dmap.height = height
        dmap.width = width
        dmap.nodes = []
        for _ in range(height):
            alts = map(int, input().split())
            line = [Node(alt) for alt in alts]
            dmap.nodes.append(line)

        return dmap

    def get_node(self, row, column):
        # If the coords are out of bounds, return a special node whose
        # altitude will never be lower than any real node, and whose label
        # will be easily spotted as a mistake if ever printed
        if row < 0 or row >= self.height or column < 0 or column >= self.width:
            return self.OutOfBounds
        else:
            return self.nodes[row][column]
        

    def render(self, altitudes=True, labels=True):
        renderlines = []
        for nodeline in self.nodes:
            renderlines.append(' '.join([n.render(altitudes, labels)
                                         for n in nodeline]))
        return '\n'.join(renderlines)

    def __str__(self):
        return self.render()

    def calc_basins(self, labelset='abcdefghijklmnopqrstuvwxyz'):
        next_li = 0
        for r in range(self.height):
            for c in range(self.width):
                l = self.label_coord(r, c, labelset[next_li])
                if l == labelset[next_li]:
                    # next label was used
                    next_li += 1

    def label_coord(self, row, column, nextlabel):
        """
        Finds the sink to label the specified node with. If that sink is
        unlabelled, it will be labelled with next label. All unlabelled nodes
        traced through to find a label will also be labelled, including the
        starting node.
        """
        node = self.get_node(row, column)
        if node.label:
            return node.label
        else:
            north = (row - 1, column)
            west = (row, column - 1)
            east = (row, column + 1)
            south = (row + 1, column)

            min = node
            min_coords = (row, column)
            for r, c in [north, west, east, south]:
                candidate = self.get_node(r, c)
                if candidate.altitude < min.altitude:
                    min = candidate
                    min_coords = (r, c)

            if min is node:
                # no lower neighbours -> this is a sink
                node.label = nextlabel
                return node.label
            else:
                r, c = min_coords
                node.label = self.label_coord(r, c, nextlabel)
                return node.label


if __name__ == '__main__':
    try:
        input()     # skip number of cases line

        caseno = 1
        while True:
            height, width = map(int, input().split())
            m = DrainageMap.readmap(height, width)
            m.calc_basins()

            print('Case #{}:'.format(caseno))
            print(m.render(altitudes=False))
            caseno += 1

    except EOFError:
        pass

