import sys

sys.setrecursionlimit(100**2 + 10)

f = open("water_in.txt")
data = f.read()
f.close()

data = data.split("\n")


s = ""
t = int(data[0])


data = data[1:]
for i in xrange(len(data)):
    data[i] = data[i].split(" ")


INDEF = '~'

def paintD(m, d, x, y, w, h, l):
    if d[y][x] != INDEF: return d[y][x]
    d[y][x] = l
    
    dx = [0, -1, 1, 0]
    dy = [-1, 0, 0, 1]
    lowerl = l

    mini = -1
    for i in xrange(4):
        cx = dx[i] + x
        cy = dy[i] + y
        if cx < 0 or cy < 0 or cx >= w or cy >= h:
            continue
        
        if m[cy][cx] < m[y][x]:
            if mini == -1:
                mini = i
            else:
                if m[cy][cx] < m[dy[mini]+y][dx[mini]+x]:
                    mini = i
    
    if mini >= 0:
        cx = dx[mini]+x
        cy = dy[mini]+y
        l2 = paintD(m, d, cx, cy, w, h, l)
        lowerl = min(lowerl, l2)
    d[y][x] = lowerl
    return lowerl

for i in xrange(t):
    print float(i) / t * 100.0
    h, w = int(data[0][0]), int(data[0][1])
    data = data[1:]
    
    m = []
    d = []
    for y in xrange(h):
        m += [[]]
        d += [[]]
        for x in xrange(w):
            m[y] += [int(data[y][x])]
            d[y] += [INDEF]

    maxl = 'a'
    l = 'a'
    for y in xrange(h):
        for x in xrange(w):
            if d[y][x] == INDEF:
                l = paintD(m, d, x, y, w, h, l)
                l = max(maxl, chr(ord(l)+1))

##    for k in m:
##        print k
##    print ""
##    for k in d:
##        print k
##    print ""
##    print "-----------"
##    print ""
    
    s += "Case #%d:\n" % (i+1)
    for y in xrange(h):
        for x in xrange(w):
            s += d[y][x]
            if x != w-1: s += " "
            else: s += "\n"
    
    data = data[h:]

print ""
print s


f = open("water_out.txt", "w")
f.write(s)
f.close()
