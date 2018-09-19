w = 0
h = 0
nextletter = 'a'

def pode(map, sx, sy, dx, dy):
    if dx < 0 or dy < 0 or dx >= w or dy >= h:
        return False
    if map[dy][dx] >= map[sy][sx]:
        return False
    return True

def procura(map, result, x, y):
    global nextletter
    
    if result[y][x] != -1:
        return result[y][x]
    
    altitude = 999999
    pos = []
    
    if pode(map, x, y, x, y + 1) and map[y + 1][x] <= altitude:
        pos = [x, y + 1]
        altitude = map[y + 1][x]
    if pode(map, x, y, x + 1, y) and map[y][x + 1] <= altitude:
        pos = [x + 1, y]
        altitude = map[y][x + 1]
    if pode(map, x, y, x - 1, y) and map[y][x - 1] <= altitude:
        pos = [x - 1, y]
        altitude = map[y][x - 1]
    if pode(map, x, y, x, y - 1) and map[y - 1][x] <= altitude:
        pos = [x, y - 1]
        altitude = map[y - 1][x]
    
    if altitude == 999999:
        result[y][x] = nextletter
        nextletter = chr(ord(nextletter) + 1)
        return result[y][x]
    else:
        result[y][x] = procura(map, result, pos[0], pos[1])
        return result[y][x]

def resolve(map):
    result = [[-1] * len(map[0]) for x in range(len(map))]
    
    for y in range(len(map)):
        for x in range(len(map[0])):
            result[y][x] = procura(map, result, x, y)
    return result

fp = open('second.in', 'r')
maps = int(fp.readline().strip())

for case in range(maps):
    parms = [int(z) for z in fp.readline().split()]
    h = parms[0]
    w = parms[1]
    
    map = []
    nextletter = 'a'
    for y in range(parms[0]):
        map.append([int(z) for z in fp.readline().strip().split()])
    
    print 'Case #' + str(case + 1) + ':'
    result = resolve(map)
    for x in range(len(result)):
        print ' '.join([str(x) for x in result[x]])
