import math
import datetime
import math


t = int(raw_input())  # read a line with a single integer
for j in xrange(1, t + 1):
    raw = raw_input()
    N = str(raw)
    N_list = list(str(raw))
    #print "origin:"+N
    numLength = len(N)
    upperRangeNumber = ""
    lowerRangeNumber = ""
    tidyNum =""
    if numLength == 1 :
        tidyNum = N
    else :
        upperRangeNumber+= N_list[0]
        for i in  range(1,numLength):
            upperRangeNumber+="9"

        lowerRangeNumber += N_list[0]
        for i in range(1, numLength):
            lowerRangeNumber += N_list[0]

        if int(N)>= int(lowerRangeNumber) and int(N)<=int(upperRangeNumber) :
            for i in range(numLength-1,0,-1):
                if int(N_list[i]) != 0 :
                    if N_list[i] < N_list[i-1] :
                        N_list[i] = "9"
                        N_list[i - 1] = str(int(N_list[i - 1])-1)
                        tidyNum = N_list[i] + tidyNum
                    else :
                        tidyNum = N_list[i] + tidyNum
                else :
                    N_list[i] = "9"
                    N_list[i - 1] = str(int(N_list[i - 1]) - 1)
                    tidyNum = N_list[i]+tidyNum

            tidyNum = N_list[0]+tidyNum

        else :
            if int(N[0]) != 1 :
                tidyNum = str(int(N_list[0])-1)
                for i in range(1, numLength):
                    tidyNum+= "9"
            else :
                tidyNum=""
                for i in range(1, numLength):
                    tidyNum+= "9"



    cnt =0

    print "Case #{}: {}".format(j, tidyNum )


