#-*-coding:utf8;-*-
#qpy:2
#qpy:console
def tide(n):
    while(n>0):
        b=True
        ns=str(n)
        i=0
        while i<len(ns)-1:
            a=ns[i]<=ns[i+1]
            if not a:
                b=False
                n=n-1
                break
            else:
                b=True
                i=i+1
        if b:
            return n                      
        
        return n
    
    
def con(n):
    ns=str(n)
    i=0
    a=""
    while i < len(ns)-1:
        a=a+ns[i]
    
        if ns[i]>ns[i+1]:
            b=int(a)
            p=len(ns)-1-i
            b=b*(10**p)
            b=tide(b)
            return b
        elif ns[i]>=ns[i+1]:
            y=i

            while ns[i]>=ns[i+1]:
                t=y
                try:
                    while ns[t]==ns[t+1]:
                        t=t+1
                        
                    if ns[t]<ns[t+1]:
                        a=a+ns[i+1]
                except IndexError:
                    pass
                        
                    
                if ns[i]>ns[i+1]:
                    b=int(a)
                    p=len(ns)-1-y
                    b=b*(10**p)
                    b=tide(b)
                    return b
                if i==len(ns)-2:
                    return int(ns)
                i=i+1
                                
        if ns[i]>ns[i+1] and ns[i+1]=="0":
            
            return tide(b)
        i=i+1
        
    return int(ns)


# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n= int(input()) 
    a=con(n)
    # read a list of integers, 2 in this case
    print("Case #{}: {}".format(i,a))
    # check out .format's specification for more formatting options
  
    
    
        
            
        
