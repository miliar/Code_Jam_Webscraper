#!/usr/bin/python

import cj
import sys

class Field(object):
    def __init__(self):
        self.locs = set()

    def add(self, x, y):
        self.locs.add((x,y))

    def has(self, x, y):
        return (x, y) in self.locs

    def go(self):
        dying = set()
        adding = set()

        for bac in self.locs:
            # check neighbors to north and west
            if not self.has(bac[0]-1,bac[1]) and not self.has(bac[0], bac[1]-1):
                dying.add(bac)
            # check neighbor to east and northeast
            if not self.has(bac[0]+1,bac[1]) and self.has(bac[0]+1,bac[1]-1):
                adding.add((bac[0]+1,bac[1]))
            # check neighbor to south and southwest
            if not self.has(bac[0],bac[1]+1) and self.has(bac[0]-1,bac[1]+1):
                adding.add((bac[0],bac[1]+1))

        self.locs.difference_update(dying)
        self.locs.update(adding)

    def size(self):
        return len(self.locs)

class Bacteria(cj.CodeJammer):

    def case(self):
        r = self.next_int()

        f = Field()
        for ri in range(r):
            x1 = self.next_int()
            y1 = self.next_int()
            x2 = self.next_int()
            y2 = self.next_int()

            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    f.add(x,y)

        c = 0
        while f.size() > 0:
            f.go()
            c += 1

        return c

if __name__ == '__main__':
    f = Bacteria(sys.argv[1])
    f.execute()   
