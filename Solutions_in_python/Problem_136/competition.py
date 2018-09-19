def checking_case(c,f,x):
    if (c>=x):
        return x/2.0
    a = 2.0
    t_all = 0
    n = c
    while (True):      
        if ((x/a) < ((c/a)+(x/(a+f)))):
            t_all += x/a
            return t_all
        t_all += (c/a)
        a+=f        
def formatting(n):
    temp = n%0.0000001
    if temp <0.00000005:
        n -= temp
    else:
        n -= (temp - 0.0000001)
    return n
    
def result(tmin,index):
    return "Case #"+str(index)+": "+str(tmin)+"\n"

fin = open("B-large.in","r")
fout = open("BLarge.txt","w") 
n = int(fin.readline())
for i in range (0,n):
    s = fin.readline()
    s = s[:-1]
    a = list(map(float,s.split()))    
    
    fout.write(result(formatting(checking_case(a[0], a[1], a[2])),i+1))
fout.close()

















    
    
