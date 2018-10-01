#stalls1
#tidyNum


def printCase(i,result):

    print("Case #{}: {} {}".format(i, result[0], result[1]))




def nextwee(stalls):
    maxGap=max(stalls)
    M=maxGap
    if M%2==0:
        maxLRS=int(M/2)
        minLRS=int((M-2)/2)
    else:
        maxLRS=int((M-1)/2)
        minLRS=int((M-1)/2)
    stalls.append(maxLRS)
    stalls.append(minLRS)
    stalls.remove(M)
    return(stalls)

def lastwee(stalls):
    maxGap=max(stalls)
    M=maxGap
    if M%2==0:
        maxLRS=int(M/2)
        minLRS=int((M-2)/2)
    else:
        maxLRS=int((M-1)/2)
        minLRS=int((M-1)/2)
    #stalls.append[maxLRS]
    #stalls.append[minLRS]
    #stalls.remove(M)
    return[maxLRS,minLRS]








#==================
t=int(input())
count=0
result="?"

for i in range(1,t+1):#+1):
    n=[int(s) for s in input().split(" ")] #,
    newnum=""
    testF=n
    stallsize=testF[0]
    wees=testF[1]
    #print(wees)
    #print(n)
    #print("i",i,t)
   # print(n[0], n[1])
    ###dostuff
    stalls=[stallsize]
    for k in range(wees-1):
       nextwee(stalls)
    result=lastwee(stalls)
    #print("result :",result)
    printCase(i,result)

