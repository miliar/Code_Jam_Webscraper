f = open("bl.in", 'r')
t =  int(f.readline())

for tb in range(t):
    label = 'a'
    h, w = [int(i) for i in f.readline().split()]
    land = []
    prog = []
    for i in xrange(h):
        land.append([int(i) for i in f.readline().split()])
        prog.append(land[-1][:])

    for y, i in enumerate(land):
        for x, j in enumerate(i):
            cx, cy = x, y
            reg = [[cx,cy]]
            while 1:
                if prog[cy][cx] > 10000:
                    break
                a = [[land[cy][cx], 0, cx, cy]]
                if cy>0: a.append([land[cy-1][cx], 1, cx, cy-1])
                if cx>0: a.append([land[cy][cx-1], 2, cx-1, cy])
                if cx<w-1: a.append([land[cy][cx+1], 3, cx+1, cy])
                if cy<h-1: a.append([land[cy+1][cx], 4, cx, cy+1])
                a.sort()
                if a[0][1] >= 3:
                    cx, cy = a[0][2], a[0][3]
                    if prog[cy][cx] > 10000:
                        for i,j in reg:
                            prog[j][i] = prog[cy][cx]
                    else:
                        reg.append([cx, cy])
                elif a[0][1] == 0:
                    for i,j in reg:
                        prog[j][i] = label
                    label = chr(ord(label)+1)
                    break
                else:
                    cx, cy = a[0][2], a[0][3]
                    if prog[cy][cx] > 10000:
                        for i,j in reg:
                            prog[j][i] = prog[cy][cx]
                        break
                    else:
                        reg.append([cx, cy])
    print "Case #"+str(tb+1)+":"
    for i in prog:
        for j in i:
            print j,
        print 
