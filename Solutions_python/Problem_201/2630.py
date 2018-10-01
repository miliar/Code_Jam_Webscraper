import math
T = int(input())

def findGaps(bathroom):
    gaps = []
    occupied = []
    for i in range(0,len(bathroom)):
        if bathroom[i]==0:
            occupied.append(i)
    for i in range(len(occupied)-1):
        gaps.append([occupied[i]+1, occupied[i+1]-1])
    return gaps

def findStall(bathroom):
    gaps = findGaps(bathroom)
    #print(gaps)
    maxdiff = -10
    maxgap = []
    for gap in gaps:
        left = gap[0]#Upper limit
        right = gap[1]#lower limit
        diff = right - left
        if diff > maxdiff:
            maxdiff = diff
            maxgap = [left,right]
    #print(maxgap)
    left = maxgap[0]
    right = maxgap[1]
    s = int(left-1 + math.ceil((right-left+1)/2))
    return s

#bathroom = [0,-1,-1,-1,0,-1,0,-1,-1,0]

#print(findGaps(bathroom))

for t in range(1,T+1):
    N, k = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    if N == k:
        print("Case #{}: {} {}".format(t,0,0))
        continue
    bathroom = [-1 for i in range(0,N+2)]
    #necessary to declare s out of loop so that it is accessible outside the loop as well.
    s = -1
    #Guards...
    bathroom[0] = 0
    bathroom[N+1] = 0
    s = N/2
    s = int(math.ceil(s))
    #print('First occupied'+str(s))
    bathroom[s] = 0
    k-=1
    while k!=0:
        s = findStall(bathroom)
        #print('occupied'+str(s))
        bathroom[s] = 0
        k-=1

    #Redefine occupied...
    occupied = []
    for i in range(0,len(bathroom)):
        if bathroom[i]==0:
            occupied.append(i)
    #print(occupied)
    #print('last occupied = '+str(s))
    i = occupied.index(s)
    #print(i)
    l = occupied[i] - occupied[i-1]-1
    r = occupied[i+1] - occupied[i]-1
    minval = min(l,r)
    maxval = max(l,r)
    #print('min = '+str(minval))
    #print('max = '+str(maxval))
    print("Case #{}: {} {}".format(t,maxval,minval))
