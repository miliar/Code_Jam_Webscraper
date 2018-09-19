def googlerecycle(a,b):
    if(a%10==0|b%10==0|a<=10|b<=10|a>=1000|b>=1000):
        return False
    sb=str(b)
    sa=str(a)
    la=len(sa)
    if(la==2):
        if((sb==sa[::-1])&(sa[0]!=sa[1])):
            return True
        else:
            return False
    elif(la==3):
        if(sa[0]==sa[1]==sa[2]):
            return False
        if((sb==sa[1:]+sa[0])|(sb==sa[2]+sa[0:2])):
            return True
        else:
            return False

f=open("input.txt")
n=f.readline()
n=int(n)
for i in range(1,n+1):
    temp=f.readline()
    li=temp.split(' ')
    a=int(li[0])
    b=int(li[1].split('\n')[0])
    
    c=0 
    for ix in range(a,b):
        for j in range(ix+1,b+1):
            if(googlerecycle(ix,j)==True):
                c=c+1
    print("Case #"+str(i)+": "+str(c),end='')
    print()
