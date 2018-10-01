import sys
from pprint import pprint

class Map:
    North = (-1,0)
    West = (0,-1)
    East = (0,1)
    South = (1,0)
    Directions = [North, West, East, South]

    def __init__(self, input):
        (self.H, self.W) = tuple([int(s) for s in input.readline().split()])
        self.M = []
        for r in xrange(self.H):
            row = [int(s) for s in input.readline().split()]
            self.M.append(row)
        self.watershed = [ [ None for x in xrange(self.W) ] for y in xrange(self.H) ]
        self.watershed[0][0] = 'a'
        self.next_label = 'b'
        self.flow(0,0,[],'a')
        for r in xrange(self.H):
            for c in xrange(self.W):
                if self.watershed[r][c] is None:
                    self.flow(r,c)

    def inside(self, r,c):
        return r >= 0 and r < self.H and c >= 0 and c < self.W

    def diff(self, r1, c1, Dir):
        (dr, dc) = Dir
        r2 = r1 + dr
        c2 = c1 + dc
        if self.inside(r2,c2):
            return self.M[r2][c2] - self.M[r1][c1]

    def move(self, r, c, Dir):
        return (r + Dir[0], c + Dir[1])

    def flow(self, r, c, trail = [], label = None):
        if label:
            if len(trail) > 0 and self.watershed[r][c]:
                for (r1,c1) in trail:
                    self.watershed[r1][c1] = label
                del trail[:]
                return
            else:
                self.watershed[r][c] = label
        bestdiff = 0
        bestdir = None
        for Dir in self.Directions:
            diff = self.diff(r,c,Dir)
            if diff and diff < bestdiff:
                bestdiff = diff
                bestdir = Dir
        if bestdir:
            if not label:
                trail.append((r,c))
            (r2,c2) = self.move(r,c,bestdir)
            self.flow(r2,c2,trail,label)
        else: # this is a sink
            if self.watershed[r][c]:
                label = self.watershed[r][c]
            else:
                label = self.next_label
                self.next_label = chr(ord(self.next_label)+1)
                self.watershed[r][c] = label
            for (r1,c1) in trail:
                self.watershed[r1][c1] = label
            del trail[:]

    def __str__(self):
        res = []
        def char(c):
            if c:
                return c
            else:
                return '.'
        for row in self.watershed:
            res.append(' '.join(map(char,row)))
        return '\n'.join(res)

def main():
    TT = int(sys.stdin.readline().strip()) # number of maps
    for t in xrange(TT):
        map = Map(sys.stdin)
        print 'Case #%d:' % (t+1)
        print map

if __name__ == "__main__":
    main()
