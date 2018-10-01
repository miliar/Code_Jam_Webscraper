#run with "python2 problemB.py <inputfile >outputfile" on arch linux

cases = input("")

for case in range(cases):
    #get input
    lawn = []    
    size = raw_input("")
    sizex = int(size.split(" ")[1])
    sizey = int(size.split(" ")[0])
    for i in range(sizey):
        lawn.append([])
        row = raw_input("").split(" ")
        for m2 in row:
            lawn[-1].append(int(m2))

    possible = True

    for setting in range(1,100):
        for i in range(sizey):
            for j in range(sizex):
                if lawn[i][j]==setting:
                    #mow vertical if possible
                    mv = True
                    for i1 in range(sizey):
                        if lawn[i1][j]==0 or lawn[i1][j]==setting:
                            pass
                        else:
                            mv = False
                            break
                    if mv:
                        for i1 in range(sizey):
                            lawn[i1][j] = 0
                    else:
                        mh = True
                        for j1 in range(sizex):
                            if lawn[i][j1]==0 or lawn[i][j1]==setting:
                                pass
                            else:
                                mh = False
                                break
                        if mh:
                            for j1 in range(sizex):
                                lawn[i][j1] = 0
                        else:
                            possible = False
    if possible:
        print "Case #%s: YES" %(case+1)
    else:
        print "Case #%s: NO" %(case+1)

