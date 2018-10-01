f = open("aero.large.in", "r")

T = int(f.readline())

N = []
W = []
L = []

R = []

for i in range(0, T):
    s = f.readline().split(" ")
    
    N.append(int(s[0]))
    W.append(int(s[1]))
    L.append(int(s[2]))
    R.append([])

    s2 = f.readline().split(" ")

    for j in range(0, N[i]):
        R[i].append((int(s2[j]), j))


f.close()

f = open("aero.out", "w")


def place(r, x, y, finallist):
    #print "place: " + str((r[0], x, y))
    finallist.append((r[1], x, y))

def remove(rlist, placelist):
    placelist = sorted(placelist)
    placelist.reverse()

    for k in placelist:
        del rlist[k]

def printer(fl, t):
    f.write("Case #" + str(t + 1) + ":")

    for u in fl:
        f.write(" " + str(u[1]) + " " + str(u[2]))

    f.write("\n")
    


for t in range(0, T):

    fl = []

    n = N[t]
    w = W[t]
    l = L[t]

    r = R[t]

    r = sorted(r)
    r.reverse()

    height = 0
    width = 0


    placelist = []
    
    place(r[0], 0, 0, fl)
    height += float(r[0][0])
    placelist.append(0)

    width += float(r[0][0])

    for i in range(1, len(r)):
        if (width + float(r[i][0])) <= w:
            place(r[i], width + float(r[i][0]), 0, fl)
            width += 2*float(r[i][0])
            placelist.append(i)

    remove(r, placelist)

    while len(r) > 0:

        width = 0

        place(r[0], 0, height + float(r[0][0]), fl)
        oldheight = height
        height += 2*float(r[0][0])
        placelist = []
        placelist.append(0)

        width += float(r[0][0])

        for i in range(1, len(r)):
            if (width + float(r[i][0])) <= w:
                place(r[i], width + float(r[i][0]), oldheight + float(r[0][0]), fl)
                width += 2*float(r[i][0])
                placelist.append(i)

        remove(r, placelist)

        if len(r) == 0:
            break

    fl = sorted(fl)

    #print str((w,l))

    printer(fl, t)


f.close()

print "done"
