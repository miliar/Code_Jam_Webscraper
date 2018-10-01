import math
def checkPalindrome(n):
    l = len(n)
    i = 0
    flag = 1
    while(l-i-1>i):
        if(n[l-i-1]!=n[i]):
            flag = 0
        i = i+1
    return flag

f = open("z.in","r")
f1  = open("b.out","w")
sz = int(f.readline().replace("\n",""))
for i in range(0,sz):
    count = 0
    rg = f.readline().split(" ")
    x = int(rg[0])
    y = int(rg[1])
    x = int(math.ceil(x**.5))
    y = int(y**.5)
    for j in range(x,y+1):
        if checkPalindrome(str(j))==1 and checkPalindrome(str(j*j))==1:
            count = count +1
    f1.write("Case #"+str(i+1)+": "+str(count)+"\n")
f1.close()
            
            
            
        
    

        
        
        
