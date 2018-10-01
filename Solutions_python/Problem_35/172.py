import pprint
class Map:
    def __init__(self, data):
        self.alts   = [map(int, d.split(" ")) for d in data]
        self.height = len(self.alts)
        self.width  = len(self.alts[0])
        self.memo   = {}
        self.names  = {}
        self.cc     = ord("a")

    def minNeighbor(self, x, y):
        cx = 0; cy = 0; cz = 20000
        if x > 0 and cz>self.alts[x-1][y]:
            cx=x-1; cy=y; cz=self.alts[x-1][y]
        if y > 0 and cz>self.alts[x][y-1]:
            cx=x; cy=y-1; cz=self.alts[x][y-1]
        if y < self.width-1 and cz>self.alts[x][y+1]:
            cx=x; cy=y+1; cz=self.alts[x][y+1]
        if x < self.height-1 and cz>self.alts[x+1][y]:
            cx=x+1; cy=y; cz=self.alts[x+1][y]            
        return cx, cy
        
    def findSink(self, x, y):
        if (x, y) in self.memo:
            return self.memo[(x, y)]
        sx, sy = self.minNeighbor(x,y)
        if self.alts[sx][sy]>=self.alts[x][y]:
            self.memo[(x, y)] = (x, y)
            return (x, y)        
        nx, ny = self.findSink(sx, sy)
#        print "R:", x, y, sx, sy, nx, ny
        self.memo[(x, y)] = (nx, ny)
        return (nx, ny)

    def nameForSink(self, x,y):
        if (x,y) not in self.names:
            self.names[(x,y)] = chr(self.cc)
            self.cc += 1
        return self.names[(x,y)]

    def __str__(self):
        s=""
        labels = [[None]*self.width]*self.height
        for x in xrange(0,self.height):
            for y in xrange(0,self.width):
                sx, sy=self.findSink(x,y)
                s+=self.nameForSink(sx, sy)+" "
            s=s[:-1]+"\n"
        return s[:-1]




maps = input()
for x in xrange(0,maps):
    h, w = raw_input().split(" ")
    d=[]
    for y in xrange(0, int(h)):
        d.append(raw_input())
    print "Case #"+str(x+1)+":"
    print Map(d)

