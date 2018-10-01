def drainmap(map, h, w):
    basins = []
    postogroup = {}
    for i in xrange(h):
        for j in xrange(w):
            lowest = getlowest(map, i, j)
            if lowest:
                if lowest in postogroup and (i,j) in postogroup:
                    for (a,b) in postogroup[(i,j)]:
                        postogroup[lowest].append((a,b))
                        postogroup[(a,b)] = postogroup[lowest]
                elif lowest in postogroup:
                    postogroup[lowest].append((i,j))
                    postogroup[(i,j)] = postogroup[lowest]
                elif (i,j) in postogroup:
                    postogroup[(i,j)].append(lowest)
                    postogroup[lowest] = postogroup[(i,j)]
                else:
                    postogroup[lowest] = [(i,j), lowest]
                    postogroup[(i,j)] = postogroup[lowest]
            else:
                basins.append((i,j))
                if (i,j) not in postogroup:
                    postogroup[(i,j)] = [(i,j)]
    basins.sort(lambda x,y: compare_basins(x,y, postogroup))
    for (name,basin) in zip('abcdefghijklmnopqrstuvwxyz', basins):
        for (i,j) in postogroup[basin]:
            map[i][j] = name

def compare_basins(x, y, postogroup):
    postogroup[x].sort()
    postogroup[y].sort()
    return cmp(postogroup[x][0], postogroup[y][0]) 
    

def getlowest(map, i, j):
    lowest = None
    checklist = [(-1,0), (0,-1), (0,1), (1,0)]
    for (a,b) in checklist:
        if map[i+a][j+b] == '#':
            continue
        if map[i+a][j+b] < map[i][j]:
            if lowest == None or map[i+a][j+b] < map[lowest[0]][lowest[1]]:
                lowest = (i+a, j+b)
    return lowest

def printmap(map):
    for row in map:
        if row[0] == '#':
            break
        print ' '.join(row[:-1])


t = int(raw_input())

for x in xrange(t):
    h, w = [int(i) for i in raw_input().split()]
    map = []
    for y in xrange(h):
        map.append(raw_input().split()+['#'])
    map.append(['#']*w)
    drainmap(map,h,w)
    print "Case #%d:" % (x+1)
    printmap(map)
