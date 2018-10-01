import sys

nmaps = int(raw_input())

def is_sink(mapa, linha, coluna):
    cell = mapa[linha][coluna]
    linha = mapa[linha]
    if (
            (coluna < len(linha) and mapa[linha][coluna + 1] < cell) or
            (coluna != 0 and mapa[linha][coluna - 1] < cell) or
            (linha < len(mapa) and mapa[linha + 1][coluna] < cell) or
            (linha != 0 and mapa[linha - 1][coluna] < cell)
            ):
        return False
    return True

def smallest(mapa, linha, coluna):
    top = (mapa[linha - 1][coluna], 1, linha - 2, coluna - 1) # north
    left = (mapa[linha][coluna - 1], 2, linha - 1, coluna - 2) # west
    right = (mapa[linha][coluna + 1], 3, linha - 1, coluna) # east
    bottom = (mapa[linha + 1][coluna], 4, linha, coluna - 1) # south
    return min([right, left, bottom, top])

from collections import defaultdict

for case in xrange(nmaps):
    height, width = map(int, raw_input().split())
    mymap = [[sys.maxint] * (width + 2)]
    for _ in xrange(height):
        line = map(int, raw_input().split())
        mymap.append([sys.maxint] + line + [sys.maxint])
    mymap.append([sys.maxint] * (width + 2))

    result = {}
    sinks = []
    for i, line in enumerate(mymap[1:-1]):
        for j, item in enumerate(line[1:-1]):
            x = smallest(mymap, i + 1, j + 1)
            if x[0] < item:
                result[(i, j)] = x[2:4]
            else:
                sinks.append((i, j))

    basins = {}
    for sink in sinks:
        basin = []
        work = []
        for k, v in result.iteritems():
            if v == sink:
                work.append(k)
                basin.append(k)
        while work:
            x = work.pop()
            for k, v in result.iteritems():
                if v == x:
                    work.append(k)
                    basin.append(k)
        basins[sink] = basin

    start = 'a'

    result = [[None] * width for _ in xrange(height)]

    mins = [(min(v + list((k,))), k) for k, v in basins.iteritems()]

    for item in sorted(mins):
        x, y = item[1]
        result[x][y] = start
        for coord in basins[item[1]]:
            x, y = coord
            result[x][y] = start
        start = chr(ord(start) + 1)

    print 'Case #%d:' % (case + 1)
    print '\n'.join([' '.join(line) for line in result])
