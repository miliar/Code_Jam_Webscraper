import sys

inputName = "B-input.txt"

if (len(sys.argv)>1):
    inputName = sys.argv[1]

inFile = open(inputName, "rt")
outFile = open(inputName+".out", "wt")

T = int(inFile.readline())
for testCase in range(1, T + 1):
    outFile.write("Case #"+str(testCase)+": ")
    line = inFile.readline().strip().split()
    N = int(line[0])
    R = int(line[1])
    O = int(line[2])
    Y = int(line[3])
    G = int(line[4])
    B = int(line[5])
    V = int(line[6])

    col=[]
    if (R>=Y) and (Y>=B):
        letters = ["R","Y","B"]
        col.append(R)
        col.append(Y)
        col.append(B)
    elif (R>=B) and (B>=Y):
        letters = ["R","B","Y"]
        col.append(R)
        col.append(B)
        col.append(Y)
    elif (B>=R) and (R>=Y):
        letters = ["B","R","Y"]
        col.append(B)
        col.append(R)
        col.append(Y)
    elif (B>=Y) and (Y>=R):
        letters = ["B","Y","R"]
        col.append(B)
        col.append(Y)
        col.append(R)
    elif (Y>=B) and (B>=R):
        letters = ["Y","B","R"]
        col.append(Y)
        col.append(B)
        col.append(R)
#    elif (Y>=R) and (R>=B):
    else:
        letters = ["Y","R","B"]
        col.append(Y)
        col.append(R)
        col.append(B)

#   print letters
#    print col
    ring=[]
    ring.append(letters[0])
    col[0]-=1;
    overall = True
#    print "started with ", letters[0]
    for j in range (N-1):
        possible = False
        pick = -1
        for k in range(3):
            if (col[k]<=0):
#                print "no more ",letters[k]
                continue
            if (letters[k]==ring[-1]):
#                print "cannot place ", letters[k]
                continue
            possible = True
            if (pick<0):
#                print "so ", letters[k], " is possible"
                pick=k
            elif (col[pick]<col[k]):
#                print "seems ",letters[k], " is more"
                pick=k
        if (possible == False):
            overall = False
            break
        else:            
            ring.append(letters[pick])
            col[pick]-=1
#            print "okay placed ", letters[pick]

    if (overall == True) and (ring[0] == ring[-1]):
#        print "start and end are the same"
        overall = False

    if (overall == False):
        outFile.write("IMPOSSIBLE")
#        print "IMPOSSIBLE"
    else:
        for j in range(N):
            outFile.write(ring[j])
#            print ring[j],
    
    outFile.write("\n")
#    print "\n------------\n"

inFile.close()
outFile.close()


