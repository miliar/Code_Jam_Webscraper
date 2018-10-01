import sys
stdin = sys.stdin

def explore(karta, y, x):
    directions = {}
    meaning = ['v', '^', '>', '<']
    for id, d in enumerate([(0, 1), (0, -1), (1, 0), (-1, 0)]):
        cx, cy = x, y
        while True:
            cx += d[0]
            cy += d[1]
            if not (0 <= cx < len(karta[0])
            and     0 <= cy < len(karta)):
                break
            if '.' != karta[cy][cx]:
                #print "c", cx, cy, karta[cy][cx]
                directions[id] = 1
                break

    #print "d", directions
    return (len(directions) >= 1, meaning.index(karta[y][x]) not in directions)
                
            

T = int(stdin.readline())
for icase in range(1, T+1):
    print 'Case #%d:' % icase,
    r, c = map(int, stdin.readline().strip().split())
    karta = []
    for y in range(r):
        karta.append(stdin.readline().strip())

    fixable = True
    nfix = 0
    for y in range(r):
        if not fixable: break
        for x in range(c):
            if '.' != karta[y][x]:
                ok, needs_fix = explore(karta, y, x)
                #print ok, needs_fix
                fixable = fixable and ok
                if not ok:
                    break
                nfix += needs_fix

    if not fixable:
        print "IMPOSSIBLE"
    else:
        print nfix

            


