import sys
#from numpy import *
from datetime import datetime

print datetime.now()
#iFName = "d:\\projekty\\google-jam\\runda-2\\c\\A-small.in"
#iFName = "A-small-attempt0.in"
iFName = "A-large.in"
iFName = "a.txt"
iFName = "B-small-attempt0.in"
iFName = "B-large.in"
outFN = "out.txt"

iFile = open(iFName, "r")
outF =  open(outFN, "w")

verbose = False

#how many maps?
T =  int(iFile.readline())

if verbose:
    print T
                
#read the test cases
for case in range(T): #(T) :
    if verbose:
        print case, datetime.now()
    S = iFile.readline()
    if verbose:
        print S
    S = S.split()
    H = int(S[0])
    W = int(S[1])
    if verbose:
        print H, W

    mapa = {}
    basin = {}
    basIdx = 0
    basEqu = {}
    for i in range(H):
        S = iFile.readline()
        S = S.split()
        j = 0
        for s in S:
            mapa[(i, j)] = int(s)
            basin[(i,j)] = basIdx
            basEqu[basIdx] = (basIdx, True)
            j += 1
            basIdx += 1
            
    if verbose:
        print "mapa"
        for i in range (H):
            for j in range(W):
                print mapa[(i,j)],
            print
        print "basEqu"
        print basEqu

            
    for i in range(H):
        for j in range(W):
            #find smallest
            si = i
            sj = j
            val = mapa[(i,j)]
            #north
            if i - 1 >= 0:
                if mapa[(i -1, j)] < val:
                    si = i -1
                    sj = j
                    val = mapa[(si, sj)]
            #west
            if j - 1 >= 0:
                if mapa[(i, j - 1)] < val:
                    si = i
                    sj = j - 1
                    val = mapa[(si, sj)]
            #East
            if j + 1 < W:
                if mapa[(i, j+1)] < val:
                    si = i
                    sj = j + 1
                    val = mapa[(si, sj)]
            #south
            if i + 1 < H:
                if mapa[(i + 1, j)] < val:
                    si = i  + 1
                    sj = j
                    val = mapa[(si, sj)]
            #update basin data
            basEqu[basin[(i,j)]] = (basin[(si, sj)], si == i and sj == j)
            basin[(i,j)] = basin[(si, sj)]

    if verbose:
        print "Basin"
        for i in range (H):
            for j in range(W):
                print basin[(i,j)],
            print
        print "basEqu"
        print basEqu
            
    #clean up basin equivalents
    for b in range(len(basEqu)):
        aux = set([b])
        nxt, stop = b, False        
        while not stop:
           nxt, stop = basEqu[nxt]
           if nxt <> b:
               aux.add (nxt)
        if verbose:
            print b, aux
        for a in aux :
            basEqu[a] = (nxt, True)
    if verbose:
        print "basEqu"
        print basEqu

    #clean up the map
    for i in range (H):
       for j in range(W):
           basin[(i,j)], x = basEqu[basin[(i,j)]]

    if verbose:
        print "Basin"
        for i in range (H):
            for j in range(W):
                print basin[(i,j)],
            print

    #assign the names
    names = {}
    nameStr = "abcdefghijklmnopqrstuvwxyz"
    nameIdx = 0
    for i in range (H):
        for j in range(W):
            if not names.has_key(basin[(i,j)]):
               names[basin[(i,j)]] = nameStr[nameIdx]
               nameIdx += 1
            basin[(i,j)] = names[basin[(i,j)]]
                
    if verbose:
        print "Basin"
        for i in range (H):
            for j in range(W):
                print basin[(i,j)],
            print

    if verbose:
        print "Case #%(c)d:" % {'c' : case + 1}
    print >> outF , "Case #%(c)d:" % {'c' : case + 1}
    for i in range (H):
       for j in range(W):
          print  >> outF , basin[(i,j)],
       print  >> outF 
    

iFile.close()
outF.close()
print datetime.now()
