
import sys

def botRun(botQueue, botPosition, prevBot, botTime, curTime): #curTime - botTime is the lagging time
    newPosition = botQueue.pop()
    newTimeOffset = abs(botPosition - newPosition) + 1 #plus one for the time it takes to push the button
    curPosition = newPosition


    if (curTime - botTime >= newTimeOffset):
        print "MIGHT HAVE AN ERROR IN TIME OFFSETS"
        return 0
    else:
        return


if __name__ == '__main__':

    for arg in sys.argv:
        inputfilename = arg;

    #check if input string is null???

    inputfile = open(inputfilename, 'r')

    outputfile = open(inputfilename + ".out", 'w')
    numberofsets = int(inputfile.readline())

    for m in range(numberofsets):
        testcase = inputfile.readline().rstrip('\r\n').split()
        print testcase

        N = int(testcase[0])

        bothQueue = list() #overall order of precedence -- O or B
        oQueue = list() #O's queue -- a number
        bQueue = list() #B's queue -- a number

        for pushcounter in range(N):
            if (testcase[pushcounter * 2 + 1] == 'O'):
                bothQueue.append('O')
                oQueue.append(int(testcase[pushcounter * 2 + 2]))
            elif (testcase[pushcounter * 2 + 1] == 'B'):
                bothQueue.append('B')
                bQueue.append(int(testcase[pushcounter * 2 + 2]))
            else:
                print "ERROR IN READING IN NEXT BUTTON"

        print bothQueue
        print oQueue
        print bQueue


        currentTime = 1 #start with Time 1
        oPosition = 1
        bPosition = 1


        for bot in bothQueue:
            if (bot == 'O'):
                #move o
                newPosition = oQueue.pop(0)
                newTimeOffset = abs(oPosition - newPosition) + 1 #plus one for the time it takes to push the button
                oPosition = newPosition
                currentTime += newTimeOffset
                #oTime += newTimeOffset

                if (not bQueue):
                    print "done running bBots"
                elif (abs(bQueue[0] - bPosition) <= newTimeOffset):
                    bPosition = bQueue[0]
                elif (bQueue[0] > bPosition):
                    bPosition = bPosition + newTimeOffset
                else:
                    bPosition = bPosition - newTimeOffset





            elif (bot == 'B'):
                #move o
                newPosition = bQueue.pop(0)
                newTimeOffset = abs(bPosition - newPosition) + 1 #plus one for the time it takes to push the button
                bPosition = newPosition
                currentTime += newTimeOffset
                #oTime += newTimeOffset


                if (not oQueue):
                    print "done running oBots"
                elif (abs(oQueue[0] - oPosition) <= newTimeOffset):
                    oPosition = oQueue[0]
                elif (oQueue[0] > oPosition):
                    oPosition = oPosition + newTimeOffset
                else:
                    oPosition = oPosition - newTimeOffset

            print str(currentTime) + "--bPosition: " + str(bPosition)
            print str(currentTime) + "--oPosition: " + str(oPosition)





        outputline = "Case #" + str(m + 1) + ": " + str(currentTime - 1) +  "\n"
        print outputline
        outputfile.write(outputline)

