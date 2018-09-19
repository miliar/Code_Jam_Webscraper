import sys

inp = sys.stdin

N = int(inp.readline())

scoreIndex = {"X":1, "O":0}

for testCase in xrange(1, N+1):
  #  fullLines = [1]*10
    scoreLines = [[0]*10,[0]*10]
    isCompleted = True
    for i in xrange(4):
        line = inp.readline()
        for j in xrange(4):
            if line[j] == ".":
                isCompleted = False
    #            fullLines[i] = 0
     #           fullLines[4+j] = 0
      #          if i == j:
       #             fullLines[8] = 0
        #        if i == (3-j)
         #           fullLines[9] = 0
    
            elif line[j] == "T":
                scoreLines[0][i] += 1
                scoreLines[1][i] += 1
                scoreLines[0][4+j] += 1
                scoreLines[1][4+j] += 1
                if i == j:
                    scoreLines[0][8] += 1
                    scoreLines[1][8] += 1
                if i == (3-j):
                    scoreLines[0][9] += 1
                    scoreLines[1][9] += 1
           
            else:
                scoreLines[scoreIndex[line[j]]][i] += 1
                scoreLines[scoreIndex[line[j]]][4+j] += 1
                if i == j:
                    scoreLines[scoreIndex[line[j]]][8] += 1
                if i == (3-j):
                    scoreLines[scoreIndex[line[j]]][9] += 1
    
    stateDescription = ""
    if 4 in scoreLines[0]:
        stateDescription = "O won"
    elif 4 in scoreLines[1]:
        stateDescription = "X won"
    elif isCompleted:
        stateDescription = "Draw"
    else:
        stateDescription = "Game has not completed"
    
    inp.readline()
    
    print "Case #{}: {}".format(testCase, stateDescription)


