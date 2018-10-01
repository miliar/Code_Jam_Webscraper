f = open('D-small-attempt3.in', 'r')
o = open('out2.txt', 'w')
T = f.readline()
T = int(T)
for i in range(1, T+1):
    l = f.readline()
    l = l.split(' ')
    l = map(int, l)

    x = l[0]
    r = l[1]
    c = l[2]

    if r > c:
        r, c = c, r

    g = -1

    if r == 1 and c == 1:
        g = x == 1
    if r == 1 and c == 2:
        g = x == 1 or x == 2
    if r == 1 and c == 3:
        g = x == 1
    if r == 1 and c == 4:
        g = x == 1 or x == 2
    if r == 2 and c == 2:
        g = x == 1 or x == 2
    if r == 2 and c == 3:
        g = x == 1 or x == 2 or x == 3
    if r == 2 and c == 4:
        g = x == 1 or x == 2
    if r == 3 and c ==3:
        g = x == 1 or x == 3
    if r == 3 and c == 4:
        g = 1
    if r == 4 and c == 4:
        g = x == 1 or x == 2 or x == 4

    if g == 1:
        winner = "GABRIEL"
    if g == 0:
        winner = "RICHARD"
    if g == -1:
        winner = "ERROR"

    outline = "Case #%d: %s\n" % (i, winner)
    o.write(outline)

o.close()
