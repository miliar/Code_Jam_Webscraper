from copy import copy

unicorns = "ROYGBV"


def getOther(u,nums):
    ind = unicorns.find(u)
    lst = [i for i in range(ind+2,6)]+[i for i in range(ind-1)]
    
    def dist(a):        
        return lambda b:-min((a+b)%6,(a-b+6)%6)
    lst = sorted(lst,key =lambda x:-nums[x])
    return sorted(lst,key=dist(ind))
    

def getNext(tupp,indices):
    #indices = sorted(indices,key = lambda x:-tupp[x])
    
    for i in indices:       
        if tupp[i] > 0:
            tupp[i] = tupp[i] - 1
            return unicorns[i]
    return None

def result(N, R, O, Y, G, B, V):

    nums = [R, O, Y, G, B, V]
    #print("".join(a*b for a,b in zip(nums,unicorns)))
    stall = [" " for i in range(N)]
    stall[0] = getNext(nums,range(6))
    for i in range(1,N):
        #print(stall)
        before = stall[i-1]
        oth = getOther(before,nums)
        #print(oth)
        
        stall[i] = getNext(nums,oth)
        if stall[i] == None:
            return "IMPOSSIBLE"
        
    if unicorns.find(stall[0]) not in getOther(stall[N-1],nums):
        return "IMPOSSIBLE"
    return "".join(stall)

t = int(input()) 
for i in range(1, t + 1):    
    
    N, R, O, Y, G, B, V = [int(k) for k in input().split(" ")]   
    res = result(N, R, O, Y, G, B, V)
    print("Case #{}: {} ".format(i, res))
    

    
    
    
    
