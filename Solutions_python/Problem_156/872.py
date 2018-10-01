import math
T = input()

def getans(ls):
    ans = max(ls)
    for i in range(ans):
        ls.sort(reverse = True)
        mnum = ls.pop(0)
        a1,a2 = int(math.ceil(mnum/2.0)),int(math.floor(mnum/2.0))
        ls += [a1,a2]
        ans = min(ans,max(ls)+i+1 )
    return ans


for t in range(T):
    N = input()
    ls = map(int,raw_input().split(" "))
    ans = getans([l for l in ls])
    
    if 9 in ls:
        ls.sort(reverse = True)
        nine = 0
        while ls.count(9):
            ls.pop(0)
            nine += 1
        ls += [3] * (nine * 2)
        ans = min(getans(ls)+(nine * 2),ans)
    print "Case #%d: %d"%(t+1,ans)
        
        
        
            
    
