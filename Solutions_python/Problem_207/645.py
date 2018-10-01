import sys

sys.setrecursionlimit(20000000)

R, Y, B = 0, 1, 2#, 3, 4, 5
names = {
    R: 'R',
    # O: 'O',
    Y: 'Y',
    # G: 'G',
    B: 'B',
    # V: 'V'
}

def get_placement(n, colors, depth=0, res=None):
    if res == None:
        res = []
    if depth == n:
        if can_add(res, res[0]):
            return ''.join([names[z] for z in res])
        else:
            return None
    for i in colors:
        if i > n/2:
            return None
    for i in sorted(range(3), key=lambda x:colors[x], reverse=True):
        if colors[i] != 0 and can_add(res, i):
            colors[i] -= 1
            subres = get_placement(n, colors, depth+1, res + [i])
            if subres != None:
                return subres
            else:
                colors[i] += 1
    return None

def can_add(places, color):
    if len(places) == 0:
        return True
    return {
        R: places[-1] != R,# and places[-1] != O and places[-1] != V,
        Y: places[-1] != Y,# and places[-1] != O and places[-1] != G,
        B: places[-1] != B,# and places[-1] != G and places[-1] != V,
        # O: places[-1] != R and places[-1] != O and places[-1] != V and places[-1] != Y and places[-1] != O and places[-1] != G,
        # G: places[-1] != Y and places[-1] != O and places[-1] != G and places[-1] != B and places[-1] != G and places[-1] != V,
        # V: places[-1] != R and places[-1] != O and places[-1] != V and places[-1] != B and places[-1] != G and places[-1] != V
    }[color]

t = int(raw_input())
for i in xrange(1, t + 1):
    n, r, o, y, g, b, v = [int(s) for s in raw_input().split(" ")]
    places = get_placement(n, [r, y, b])
    print "Case #{}: {}".format(i, places if places != None else "IMPOSSIBLE")