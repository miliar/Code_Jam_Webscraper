#!/usr/bin/python

def readG(fd):
    G = []
    G.append(fd.readline())
    G[0] = G[0][0:4]
    G.append(fd.readline())
    G[1] = G[1][0:4]
    G.append(fd.readline())
    G[2] = G[2][0:4]
    G.append(fd.readline())
    G[3] = G[3][0:4]
    fd.readline()
    return G

def readT(fd):
    T = fd.readline()
    return int(T)

def mapping():
    m = dict(a='y', b='h', c='e', d='s', e='o', f='c', g='v', h='x', i='d',
                    j='u', k='i', l='g', m='l', n='b', o='k', p='r', q='z',
                    r='t', s='n', t='w', u='j', v='p', w='f', x='m', y='a',
                    z='q')
    #print m
    return m

    
def main(argv):
    argc = len(argv)
    if argc == 1:
        print "No input file!"
        exit(-1)
    if argc > 2:
        exit(-1)
    
    inFilename = argv[1]
    inFd = open(inFilename, "r")

    T = readT(inFd)
    #print T
    for k in range(0, T):
    #for i in range(0, 1):
        G = readG(inFd)
        #print G

        #l = len(G)
        #print l
        r_x = [0, 0, 0, 0]
        r_o = [0, 0, 0, 0]
        r_dot = [0, 0, 0, 0]
        c_x = [0, 0, 0, 0]
        c_o = [0, 0, 0, 0]
        c_dot = [0, 0, 0, 0]
        dd_x = 0
        dd_o = 0
        dd_dot = 0
        du_x = 0
        du_o = 0
        du_dot = 0
        s = ""

        for i in range(0, 4):
            for j in range(0, 4):
                if G[i][j] == "X" or G[i][j] == "T":
                    r_x[i] = r_x[i] + 1
                if G[i][j] == "O" or G[i][j] == "T":
                    r_o[i] = r_o[i] + 1
                if G[i][j] == ".":
                    r_dot[i] = r_dot[i] + 1

                if G[j][i] == "X" or G[j][i] == "T":
                    c_x[i] = c_x[i] + 1
                if G[j][i] == "O" or G[j][i] == "T":
                    c_o[i] = c_o[i] + 1
                if G[j][i] == ".":
                    c_dot[i] = c_dot[i] + 1

        for i in range(0, 4):
            if G[i][i] == "X" or G[i][i] == "T":
                dd_x = dd_x + 1
            if G[i][i] == "O" or G[i][i] == "T":
                dd_o = dd_o + 1
            if G[i][i] == ".":
                dd_dot = dd_dot + 1

            if G[3-i][i] == "X" or G[3-i][i] == "T":
                du_x = du_x + 1
            if G[3-i][i] == "O" or G[3-i][i] == "T":
                du_o = du_o + 1
            if G[3-i][i] == ".":
                du_dot = du_dot + 1

        #print r_x, r_o, r_dot
        #print c_x, c_o, c_dot
        #print dd_x, dd_o, dd_dot
        #print du_x, du_o, du_dot

        s = ""

        # check if X won
        if s == "":
            for i in range(0, 4):
                if r_x[i] == 4 or c_x[i] == 4:
                    s = "X won"
                    break
                if dd_x == 4 or du_x == 4:
                    s = "X won"
                    break

        # check if O won
        if s == "":
            for i in range(0, 4):
                if r_o[i] == 4 or c_o[i] == 4:
                    s = "O won"
                    break
                if dd_o == 4 or du_o == 4:
                    s = "O won"
                    break

        # check if Draw
        if s == "":
            if r_dot[0] == 0 and r_dot[1] == 0 and r_dot[2] == 0 and r_dot[3] == 0:
                s = "Draw"

        # check if Game has not completed
        if s == "":
            s = "Game has not completed"

        print 'Case #'+str(k+1)+':',
        print s
            

    inFd.close()
    exit(0)


if __name__ == "__main__":
    import sys
    main(sys.argv)



    

