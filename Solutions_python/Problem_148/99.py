#!/usr/bin/python

def doit():
    #print repr(st)
    a=raw_input().split()
    b=raw_input().split()
    
    N = int(a[0])
    X = int(a[1])
    
    d = []
    for aa in b:
        d.append(int(aa))
        
    d.sort()
    
    i = 0
    j = N-1
    r = 0
    
    #print repr(d)
    
    while i <= j:
        r+=1
        #print i,j
        if d[i] + d[j] > X:
            j-=1
        else:
            j-=1
            i+=1
            
    print r
    

    

cases = input()
for case in range(1, cases+1):
    
    print ("Case #" + str(case) + ":"),
    doit()
    
        
