

fout = open('out.txt','w')
with open('in.txt') as f:
    T = int(f.readline())
    for case in range(1,T+1):
        line = f.readline()

        line = line.split()
        n = int(line[0])
        c = int(line[1])
        m = int(line[2])

        d = {}
        for i in range(m):
            line = f.readline()
            line = line.split()
            pi = int(line[0])
            bi = int(line[1])
            if bi not in d:
                d[bi] = []
            d[bi].append(pi)
        for pis in d.values():
            pis.sort()

        #small
        if c == 2:
            c1 = d[1] if 1 in d else []
            c2 = d[2] if 2 in d else []
            ups = 0
            rides = 0
            while c1 and c2:
                rides += 1
                if c1[0] > c2[0]:
                    c2,c1 = c1,c2
                p1 = c1.pop(0)
                #duplicates first, then largest available, then upgrade
                for p2 in c2:
                    if p2 > p1 and p2 in c1:
                        c2.remove(p2)
                        break
                else:
                    for p2 in c2:
                        if p2 > p1:
                            c2.remove(p2)
                            break
                    else:
                        if p1 != 1:
                            p2 = c2.pop(0)
                            ups += 1
            rides += len(c1)
            rides += len(c2)
        else:
            ups = 0
            rides = 0

        str = "Case #%d: %d %d\n" % (case, rides, ups)
        print str,
        fout.write(str)
fout.close()
