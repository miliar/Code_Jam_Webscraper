def is_valid(t, w, h):
    return True if t[0] >= 0 and t[0] < h and t[1] >=0 and t[1] < w else False

def flow(m, b, x, y, w, h, c):
    if not b[x][y]:
        b[x][y] = c
    else:
        return b[x][y]

    c1 = (x-1, y)
    c2 = (x, y-1)
    c3 = (x, y+1)
    c4 = (x+1, y)
    
    t1 = None
    min = m[x][y]
    if is_valid(c1, w, h) and min > m[c1[0]][c1[1]]: 
        t1 = c1
        min = m[c1[0]][c1[1]]
    if is_valid(c2, w, h) and min > m[c2[0]][c2[1]]: 
        t1 = c2
        min = m[c2[0]][c2[1]]

    if is_valid(c3,w,h) and min > m[c3[0]][c3[1]]: 
        t1 = c3
        min = m[c3[0]][c3[1]]

    if is_valid(c4,w,h) and min > m[c4[0]][c4[1]]: 
        t1 = c4
        min = m[c4[0]][c4[1]]
    
    if t1:
        c = flow(m, b, t1[0], t1[1], w, h, c)
        b[x][y] = c
        return c
    return c


fin = open("B-large.in")
t = int(fin.readline())

for i in xrange(t):
    map = []
    res = []
    tmp = fin.readline()
    tmp = tmp.replace(" ",",")
    h,w = eval(tmp)

    for j in xrange(h):
        tmp = fin.readline()
        tmp = tmp.replace(" ",",")
        map.append( eval( "[%s]" % tmp ) )
        res.append( [''] * len(map[0]) )
    
    character = 97 
    for x in xrange(h):
        for y in xrange(w):
            if x == 0 and y == 0:
                c = flow( map, res, 0,0, w,h, 'a' )
                res[x][y] = c
            elif res[x][y]:
                continue
            else:
                character += 1
                c=flow( map, res, x, y, w,h, character )
                res[x][y] = c


    character = 98
    charmap = {}
    for x in xrange(h):
        for y in xrange(w):
            if type(res[x][y]) == type(1):
                if res[x][y] not in charmap:
                    charmap[res[x][y]] = chr(character)
                    character += 1

                res[x][y] = charmap[res[x][y]] 
    print "Case #%d:"   % (i+1)
    for r in res:
        print " ".join(r)


