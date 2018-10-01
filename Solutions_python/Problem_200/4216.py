import math

def checkNum(x):
    cond = 1
    if(int(math.log10(x))+1 == 1):
        return cond;
    prevDigit=x%10
    x=int(x/10);
    for i in range(int(math.log10(x))+1):
        Digit = x%10
        if(Digit>prevDigit):
            return 0
        prevDigit=Digit
        x=int(x/10)
    return cond


t=input();
for i in range(int(t)):
    x=input();
    for j in range(int(x),-1,-1):
        if(checkNum(j)==1):
            print("Case #"+str(i+1)+": "+str(j))
            break
