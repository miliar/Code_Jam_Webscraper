t = int(raw_input())
import math
b = "Case #"
for i in range(t):
    y = raw_input().split()
    y = [int(j) for j in y]
    r,x = y
    pi = math.pi
    z = x/pi
    k=r+1
    a = (k*k)-(r*r)
    count = 01
    while a<=x:
        k+=2
        r+=2
        l = (k*k)-(r*r)
        #print l
        a+= (k*k)-(r*r)
        count+=1
    print b+str(i+1)+": "+str(count-1)
