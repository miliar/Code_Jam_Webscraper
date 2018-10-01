t=int(input())
for z in range(t):
    n= int(input())
    for i in range(n,-1,-1):
        l=[]
        a=i
        x=i%10
        while(i>0 and x!=0):
            x=i%10
            l.append(x)
            i=i//10
        if 0 not in set(l) and i<=0:
            if len(l)==1:
                print("case #",end='')
                print(z+1,end=': ')
                print(a)
                break
            l.reverse()
            if l==sorted(l):
                print("case #",end='')
                print(z+1,end=': ')
                print(a)
                break
            
        
            
