import sys

class Tiles:
    def __init__(self, data, w, h):
        self.data = data
        self.width = w
        self.height = h

    def checkVertical(self):
        for x in range(0, self.width):
            count = 0
            for y in range(0, self.height):
                tile = self.data[y][x]
                if tile == '#':
                    count += 1
            if count % 2 != 0:
                return False
        return True

    def checkHorizontal(self):
        for y in range(0, self.height):
            count = 0
            for x in range(0, self.width):
                tile = self.data[y][x]
                if tile == '#':
                    count += 1
            if count % 2 != 0:
                return False
        return True

    def isPossible(self):
        return self.checkVertical() and self.checkHorizontal()

    def isRedTile(self, char):
        return char == '/' or char == '\\'

    def split(self, seq):
        result = []
        for c in seq:
            result.append(c)
        return result

    def createRedWhiteTile(self):
        result = [ self.split(c) for c in self.data[:] ]
        for y in range(0, self.height):
            for x in range(0, self.width):
                tile = self.data[y][x]
                if tile == '#' and not self.isRedTile(result[y][x]):
                    result[y][x] = '/'
                    result[y+1][x] = '\\'
                    result[y][x+1] = '\\'
                    result[y+1][x+1] = '/'
        return Tiles(result, self.width, self.height)

    def __repr__(self):
        ret = []
        for line in self.data:
            ret.append(''.join(line))
        return '\n'.join(ret)

def eatTile(lines, height):
    result = []
    for i in range(0, height):
        result.append(lines.pop(0))
    return result

def main():
    lines = [line.rstrip() for line in open(sys.argv[1])]
    lines.pop(0)
    count = 1
    while len(lines) != 0:
        (R, C) = [int(v) for v in lines.pop(0).split()]
        tileData = eatTile(lines, R)
        tiles = Tiles(tileData, C, R)
        if tiles.isPossible():
            print 'Case #%d:' % count
            print tiles.createRedWhiteTile()
        else:
            print 'Case #%d:\n%s' % (count, 'Impossible')
        count += 1

if __name__ == '__main__':
    main()
