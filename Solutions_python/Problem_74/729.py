def printMove(T):
    if T[1] is ' ':
            N=int(T[0])
            T=T[2:].split()
    elif T[2] is ' ':
            N=(10*int(T[0]))+int(T[1])
            T=T[2:].split()
    else:
        N=(100*int(T[0]))+(10*int(T[1]))+int(T[2])
        T=T[3:].split()
    
    #print "N is ",N
    O={'goingToPress' : False, 'currPos' : 1}
    B={'goingToPress' : False, 'currPos' : 1}
    moveCount = 0
    otherMoveCount = 0;
    globalTime=1

    for i in xrange(0,2*N,2):
            T[i+1]=int(T[i+1])

            
    for i in xrange(0,2*N,2):
            #print "\n\nGLOBAL TIME",globalTime
            #print T[i],T[i+1]
            if T[i] is 'O':
                    moveCount = T[i+1] - O['currPos']
                    globalTime = globalTime + abs(moveCount) + 1
                    #print "O pushed at:",globalTime - 1 
                    O['currPos'] = T[i+1]
                    moveCount = abs(moveCount) +1
                    j=i+2
                    while j < 2*N and T[j] is not 'B':
                        j = j + 2
                    if j < 2*N and T[j] is 'B':
                        otherMoveCount = T[j+1] - B['currPos']
                        
                        #print "OtherMoveCount: ", otherMoveCount, "\nMoveCount: ", moveCount
                        if abs(otherMoveCount) <= abs(moveCount):
                                B['currPos'] = T[j+1]
                        else:
                            if B['currPos'] < T[j+1]:
                                    B['currPos']  = B['currPos'] + abs(moveCount)
                            else: B['currPos']  = B['currPos'] - abs(moveCount)
                       # print "B is now at: ", B['currPos']
                   # print T, O['currPos'], moveCount
                        

                            
            elif T[i] is 'B':
                    moveCount = T[i+1] - B['currPos']
                    globalTime = globalTime + abs(moveCount) + 1
                    #print "B pushed at:",globalTime - 1
                    B['currPos'] = T[i+1]
                    moveCount = abs(moveCount) +1
                    j=i+2
                    #print i
                    while j < 2*N and T[j] is not 'O':
                        j = j + 2
                    #print j,N
                    #print j < 2*N
                    #if j < 2*N :
                            #print "HELLO"
                            #print T[j], T[j] is 'O'
                    if j < 2*N and T[j] is 'O':
                        otherMoveCount = T[j+1] - O['currPos']
                       # print "OtherMoveCount: ", otherMoveCount, "\nMoveCount: ", moveCount
                        if abs(otherMoveCount) <= abs(moveCount):
                                O['currPos'] = T[j+1]
                        else:
                            if O['currPos'] < T[j+1]:
                                    O['currPos']  = O['currPos'] + abs(moveCount)
                            else: O['currPos']  = O['currPos'] - abs(moveCount)
                       # print "O is now at: ", O['currPos']
                   # print T, B['currPos'], moveCount
    #print globalTime-1     
    return globalTime-1

import sys
#sys.stdin.close()
sys.stdin = open("in.txt", "r")

sys.stdout = open("out.txt", "w") 
no = input()
for i in xrange(0,no):
    INP = raw_input()
    print "Case #{0}: {1}".format(i+1,printMove(INP))

sys.stdout.close()
