#!/usr/bin/env python2.6
MAX_altitude = 100000

def setup(W, H):
    map = { (-1, -1): MAX_altitude }
    queue = []
    for y in range(H):
        row = [int(d) for d in raw_input().split()]
        for x in range(W):
            map[(x, y)] = row[x]
            queue.append((x, y))
    queue.sort(lambda a, b: cmp(map[b], map[a]))
#    print map, queue
    return map, queue

vec = ((0, -1), (-1, 0), (1, 0), (0, 1))

def calc(W, H, map, queue):
    result = {}
    unused = 0
    for pos in queue:
        path = []
        next = (-2, -2)
        while next != (-1, -1) and not (pos in result):
            path.append(pos)
            lowest = map[pos]
            next = (-1, -1)
            for v in vec:
                goto = move(pos, v)
                h = map[goto]
                if h < lowest:
                    lowest = h
                    next = goto
            pos = next
#            print("goto ", pos)
        if pos in result:
            mark = result[pos]
        else:
            mark = unused
            unused += 1
        for pos in path:
            result[pos] = mark
    return result
        
def move(p, v):
    next = (p[0] + v[0], p[1] + v[1])
    if next[0] < 0 or next[1] < 0 or next[0] >= W or next[1] >= H:
        return (-1, -1)
    return next

def paint(map):
    symbol = ord('a')
    alpha = {}
    for y in range(H):
        row = ""
        for x in range(W):
            owner = map[(x, y)]
            if not owner in alpha:
                alpha[owner] = chr(symbol)
                symbol += 1
            row += alpha[owner] + " "
        print(row)

#
# main
#
T = int(raw_input())
for i in range(T):
    print("Case #%d:" % (i + 1))
    H, W = [int(d) for d in raw_input().split()]
    map, queue = setup(W, H)
    result = calc(W, H, map, queue)
    paint(result)
