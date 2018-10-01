import sys,math

numOfTests= int(sys.stdin.readline())
for i in range(numOfTests):
    line = sys.stdin.readline().split()
    maxToday = int(line[0])
    percentWinToday = int(line[1])
    percentWinTotal = int(line[2])
    possible = False
    for j in range(1,maxToday+1):
        if j*percentWinToday %100 == 0: #day percent is possible
            lostToday = j-percentWinToday*j/100
            winToday = (percentWinToday*j/100)

            if not ((lostToday != 0 and percentWinTotal == 100)
                    or (winToday != 0 and percentWinTotal == 0)):
                print "Case #" + str(i+1) + ": Possible"
                possible = True
                break
    if possible == False:
        print "Case #" + str(i+1) + ": Broken"      
