import math
def listincrease(l,p):
    a = l[p]
    if a%2==1:
        t = (a-1)/2
        
        l[p]=t
        l.insert(p+1,t)
        s=[t,t]
        
    else:
        t = a/2
        l[p]=t-1
        l.insert(p+1,t)
        s=[t-1,t]
    return s

    

b= int(input())
for i in range(b):
    n,it = (input().split())
    n = int(n)
    it = int(it)
    lst =[n]
    maxi = 0
    for j in range(it):
        maxi = lst.index(max(lst))
        w = listincrease(lst,maxi)
    print("Case #"+str(i+1)+':',int(max(w)),int(min(w))) 
        
    

