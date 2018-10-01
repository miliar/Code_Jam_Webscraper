from __future__ import print_function

import time
import sys
def doit(s,D,leng,numSwaps):
    # aud = list(audStr)
    # if(leng==1):
    #     return s[0]

    if((s[0]==9)&(leng==1)):
        return 5
    s.sort()
    
    # med = getMean(s,leng)
    maxMin = max(s)
    leng = len(s)    
    swapCnt =0
    minCnt= 0
    #if max is diff from min by 1 then special minute else 
    #subtract 1
    # would work faster overall if use sorted list
    # sort after each switch
    nonZero = True
    while(nonZero):
        # print ("arr")
        # print (str(s).strip('[]'))     
        # print (str(minCnt))
        minCnt +=1
        arrSwap = swap(s[:],leng)


        maxSwap =  max(arrSwap)

        if(numSwaps>swapCnt):
            s = arrSwap[:]
            leng +=1
        else:
            arrSub = sub(s[:],leng)
            s = arrSub[:]
        if(minCnt>maxMin):
            return maxMin
        swapCnt +=1
        nonZero = contSub(s,leng)
    if(maxMin<minCnt):
        minCnt = maxMin
    return minCnt



def swap(arr, leng):
    arr.append(0)
    arr.sort()
    leng = len(arr)

    avg = int((arr[leng-1])/2)
    # if(int(arr[leng-1])==9):
    #     for i in range(leng-2):
    #         if(arr[leng-2-i]>=6):
    #             avg = 4
    #             break
    #         avg=6
    diff = arr[leng-1]-avg
    arr[0] += diff
    arr[leng-1] -= diff
    arr.sort()
    return arr[:]
def sub(arr,leng):
    for i in range(leng):
        arr[i] -= 1
        if(arr[i]<0):
            arr[i] = 0
    return arr[:]

def contSub(arr, leng):
    for x in arr:
        if(x>0):
            return True
    return False

def outP(cNum, name):
    # print("Case #" + str(cNum) + ": " +str( mNumf)+ "\n")
    # f = open('out','w')

    gab = "GABRIEL"
    # print("Case #" + str(cNum) + ": " +str( mNumf), file=f)
    with open('out.txt','a') as oFile:
        oFile.write("Case #" + str(cNum) + ": " +name+"\n")

def breakblock(_t,s):
    # c = int(s[0])

    # aud = (s[1])
    zCnt = doit(s)
    outP(_t+1,zCnt)


def sumCritArr(arr, extras):
    sumC = extras
    for i in range(len(arr)):
        if(i<=sumC):
            sumC += (arr[i])
            continue    
        break
    return sumC

def getMinPath(s,D,leng):
    minV = D
    for i in range(minV+1):
        nMin1 = doit(s,D,len(s),i)
        
        if(nMin1<minV):
            minV = nMin1
    return minV

if __name__ == "__main__":

    gab = "GABRIEL"
    ric = "RICHARD"
    # file1 = "t1"
    file1 = "D-small-attempt4.in"
    # file1 = "t1"
    f = open(file1)
    t = int(f.readline())
    tSum = 0
    for _t in xrange(t):
        s = (f.readline().split())
        s = map(int, s)
        X = s[0]
        R = s[1]
        C = s[2]
        if((X>R)&(X>C)):
            outP(_t+1,ric)
        elif((X>4)):
            outP(_t+1,ric)
        elif(X==1):
            outP(_t+1,gab)
        elif(X==3):
            if((R*C==6)|(R*C==9)|(R*C==12)):
                outP(_t+1,gab)
            else:
                outP(_t+1,ric)
        elif(X==2):
            if(((R*C)%2==0)&(C*R>1)):
                outP(_t+1,gab)
            else:
                outP(_t+1,ric)
        elif(X==4):
            if((R*C==16)|(R*C==12)):
                outP(_t+1,gab)
            else:
                outP(_t+1,ric)
        else:
            print("wtf")

    #623
    #714 maxing
    #635 new stiless
    #593 new styles!
    #701
    #701
    #621 with min strat
    #605 adjusted

    #896 for first case
    # for simply subtracing indicating this is significantly better
    #- 358


    # 696 with optimise...
    # 696 wiht normal subs
    #with med 628
    #619 wiht mean
    #696 with optimise..
    #621 wiht min strat
    # sTest = "11111"
    # sTest1 = "09"
    # sTest2 = "110011"
    # sTest3 = "1"
    # breakblock(1,sTest)
    # breakblock(2,sTest1)
    # breakblock(3,sTest2)
    # breakblock(4,sTest3)

    # doit(sTest)
    # doit(sTest1)
    # doit(sTest2)
    # doit(sTest3)



    # f = sys.stdin

    # if len(sys.argv) >= 2:
    #     fn = sys.argv[1]
    #     if fn != '-':
    #         f = open(fn)
