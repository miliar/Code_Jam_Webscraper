import sys
import string
import math


def main():
    f=open(sys.argv[1],'r')
    times=f.readline()
    times=int(times)
    for j in range(0,times):
        count=0
        num=f.readline()
        x=num.split(' ',1)[0]
        y=num.split(' ',1)[1]
        x=int(x)
        y=int(y)
        y=y+1
        nu1=x
        nu2=y
        for i in range(x,y):
            z=math.sqrt(i)
            z=str(z)
            m=z.split('.',1)[1]
            m=int(m)
            if(m==0):
                
                number=pal(i)
                root=palr(z)
                if(root==1 and number==1):
                    count=count+1
            else:
                continue
        
        print ('Case #'+str(j+1)+': '+str(count))
def pal(z):
    z=float(z)
    z=int(z)
    z=str(z)
    length=len(z)
    check=0
    if(length>1):
        for i in range(0,int(length/2)):
            if (z[i]==z[length-i-1]):
                check=10
            else:
                break
    else:
        check=10


        
    if (check==10):
        return(1)
        
def palr(z):
    z=float(z)
    z=int(z)
    z=str(z)
    length=len(z)
    check=0
    if(length>1):
        for i in range(0,int(length/2)):
            if (z[i]==z[length-i-1]):
                check=10
            else:
                break
    else:
        check=10


        
    if (check==10):
        return(1)    
    
if __name__== '__main__':
    main()
