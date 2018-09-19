from sys import stdin

C = int(stdin.readline())

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def gcdlist(list):
    nwd = list[0]
    for i in xrange(1,len(list)):
        nwd = gcd(nwd,list[i])
        
    return nwd

for c in xrange(0,C):
    nums = stdin.readline()
    nums = nums.split()
    N = int(nums[0])
    nums = [int(x) for x in nums]
    nums.pop(0)
    nums.sort()
    nums.reverse()
    mods=[]
    lnwd = gcdlist(nums)
    if (lnwd!=1):
        for i in xrange(0,N):
            nums[i]/=lnwd
    
    for i in xrange(0,N-1):
        res = nums[i]-nums[i+1]
        mods.append(res)
    
    nwd = mods[0]
    for i in xrange(1,len(mods)):
        nwd = gcd(nwd,mods[i])
    
#    print "mods:",mods
#    print "nwd:",nwd
    
    res = 0    
    if nwd>1:
        res = nums[0]+nwd
        res%=nwd
        res = nwd-res
    
    print "Case #"+str(c+1)+":",res*lnwd
        
