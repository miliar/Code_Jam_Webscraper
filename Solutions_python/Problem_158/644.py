def omino_gen(x):
    if x == 1:
        yield [(0,0)]
        return
    for smaller in omino_gen(x-1):
        for spot in smaller:
            for x in range(-1,2):
                new_spot = (spot[0] + x, spot[1])
                if new_spot not in smaller:
                    yield smaller + [new_spot]
            for y in range(-1,2):
                new_spot = (spot[0], spot[1] + y)
                if new_spot not in smaller:
                    yield smaller + [new_spot]

def rotate(o):
    return [(y, -x) for x, y in o]

def reflect(o):
    return [(-x,y) for x,y in o]

def all_combos(o):
    yield o
    a = o
    for i in range(3):
        a = rotate(a)
        yield a
    r = reflect(o)
    yield r
    a=r
    for i in range(3):
        a=rotate(a)
        yield a

def solve(x, r, c):
    for omino in omino_gen(x):
        found = False
        for row in range(r):
            if found:
                break
            for col in range(c):
                if found:
                    break
                for combo in all_combos(omino):
                    placement = set((row + i, col + j) for i, j in combo)
                    if not all(0 <= i < r and 0 <= j < c for i,j in placement):
                        continue
                    open_spots = set((i,j) for i in range(r) for j in range(c))
                    open_spots -= placement
                    good = True
                    while open_spots and good:
                        for cur in open_spots:
                            break
                        open_spots.remove(cur)
                        count = 1
                        q = [cur]
                        while q:
                            cur = q.pop()
                            for dr in range(-1,2):
                                test = (cur[0]+dr, cur[1])
                                if test in open_spots:
                                    open_spots.remove(test)
                                    count += 1
                                    q.append(test)
                            for dc in range(-1,2):
                                test = (cur[0], cur[1]+dc)
                                if test in open_spots:
                                    open_spots.remove(test)
                                    count += 1
                                    q.append(test)
                        if count % x != 0:
                            good = False
                    if good:
                        found = True
                        break
        if not found:
            return False

    return True

cases = int(input())
for t in range(1, cases+1):
    x, r, c = tuple(int(s) for s in input().split(' '))
    res = 'GABRIEL' if solve(x, r, c) else 'RICHARD'
    print('Case #%d: %s' % (t, res))
