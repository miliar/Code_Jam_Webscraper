import sys


letters = [chr(i) for i in xrange(ord('a'), ord('z') + 1)]


def parse_input(file):
    T = int(file.readline())

    for i in xrange(T):
        H, W = map(int, file.readline().split())
        geomap = []
        for j in xrange(H):
            geomap.append(map(int, file.readline().split()))
        yield geomap


def is_sink(x, y, geomap, H, W):
    coords = [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]
    for i, j in coords:
        if i >= 0 and j >= 0 and i < W and j < H:
            if geomap[y][x] > geomap[j][i]:
                return False
    else:
        return True


def find_sinks(geomap):
    H, W = len(geomap), len(geomap[0])
    sink_map = []
    least_num = 1
    for y in xrange(H):
        row = []
        for x in xrange(W):
            if is_sink(x, y, geomap, H, W):
                row.append(least_num)
                least_num += 1
            else:
                row.append(0)
        sink_map.append(row)
    return sink_map


def find_basin(x, y, sink_map, geomap, H, W):
    if sink_map[y][x] != 0:
        return sink_map[y][x]
    neighbours = []
    coords = [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]
    for n, (i, j) in enumerate(coords):
        if i >= 0 and j >= 0 and i < W and j < H:
            neighbours.append((geomap[j][i], n, (i, j)))
    next = min(neighbours)
    next_x, next_y = next[2]
    basin = find_basin(next_x, next_y, sink_map, geomap, H, W)
    return basin


def paint_map(sink_map, geomap):
    H, W = len(geomap), len(geomap[0])
    for x in xrange(W):
        for y in xrange(H):
            if sink_map[y][x] == 0:
                sink_map[y][x] = find_basin(x, y, sink_map, geomap, H, W)

    return sink_map


def letter_map(paint_map):
    H, W = len(paint_map), len(paint_map[0])
    min_letter = 0
    letter_dict = {}

    for y in xrange(H):
        for x in xrange(W):
            c = paint_map[y][x]
            if paint_map[y][x] not in letter_dict:
                new_letter = letters[min_letter]
                min_letter += 1
                letter_dict[c] = new_letter

    res_map = []

    for y in xrange(H):
        row = []
        for x in xrange(W):
            row.append(letter_dict[paint_map[y][x]])
        res_map.append(row)

    return res_map


def main():
    fnames = sys.argv[1:3]
    inp = open(fnames[0], 'rt')
    outp = open(fnames[1], 'wt')

    for n, geomap in enumerate(parse_input(inp)):
        sink_map = find_sinks(geomap)
        outp.write('Case #%d:\n' % (n+1))
        res_map = letter_map(paint_map(sink_map, geomap))
        for row in res_map:
            outp.write(' '.join(row) + '\n')

    outp.close()


if __name__ == '__main__':
    main()

