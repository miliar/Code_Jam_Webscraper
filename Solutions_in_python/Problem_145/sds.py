from math import *

def powTwoBit(number):
  return (number & (number-1) == 0) and (number != 0)

def check(y,x):
    if(y%x!=0 and y>x and powTwoBit(int(y))):
        return True
    elif(y%x==0 and y>x and powTwoBit(int(y/x))):
        return True
    else:
        return False
        

n=input()
n=int(n)


for i in range(1,n+1):
    stri=input()
    x=int(stri[0:stri.find('/')])
    y=int(stri[stri.find('/')+1:len(stri)])
    cnt=0
    if(x==1 and y==1):
        print("Case #"+str(i)+": "+str(cnt))
    elif(int(y)%2!=0):
        print("Case #"+str(i)+": impossible")
    elif(not check(y,x)):
        print("Case #"+str(i)+": impossible")
    else:
        while(cnt<40):
            cnt=cnt+1
            x=2*x
            if(x-y>=0):
                print("Case #"+str(i)+": "+str(cnt))
                break
            
            
    
        

(y>x) and not powTwoBit(int(y/x))
