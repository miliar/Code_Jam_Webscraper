import math

pi = math.pi

testcase = int(input())

for tc in range(1, testcase+1):

    linestr = input()
    N = int(linestr.split(" ")[0])
    K = int(linestr.split(" ")[1])

    ans = [] # ans[t]: pop k-1 in 1~t-1 and pop t 
    radius = []
    pirr = []
    
    height = []
    rh = []
    for i in range(N):
        linestr = input()
        tempR = int(linestr.split(" ")[0])
        tempH = int(linestr.split(" ")[1])
        radius.append(tempR)
        height.append(tempH)
        ans.append(0)
        pirr.append((tempR*tempR, 2*tempR*tempH))
        #rh.append((tempR*tempH, tempR, tempH))

    rh.sort()
    _2pirh = []
    
    #print(rh)

    pirr.sort()
    #print(pirr)
    for i in range(N):
        _2pirh.append(pirr[i][1])

    '''
    tempR = []
    s = 0
    for i in range(K):
        tempR.append(rh[i][1])
        s += rh[i][0] * 2 * pi # 2 pi r h
    maxR = max(tempR)
    s += maxR*maxR*pi
    ans.append(s)

    for i in range(K, N):
        s = 0
        tempR.append(rh[i][1])
        if tempR[0] >= maxR:
            maxR = max(tempR[1:])
        del tempR[0]
    '''

    '''
    totalsum = 0
    sidesum = []
    for i in range(N):
        totalsum += pirr[i][0]
    '''
    #print("N=", N, ", K=", K)
    maxans = 0    
    for i in range(K-1, N):
        #print(sorted(_2pirh[:i])[-(K-1):])
        if K>1:
            s = sum((sorted(_2pirh[:i]))[-(K-1):])
        else:
            s = 0
        s += pirr[i][0] + pirr[i][1]
        if maxans < s:
            maxans = s
       
    print("Case #"+str(tc)+": "+str(maxans*pi))
