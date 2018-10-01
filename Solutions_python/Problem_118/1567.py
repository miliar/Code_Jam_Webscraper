import string
import math
from goto import goto, comefrom, label

finn=open('C:/Users/HP/Desktop/input.txt','r')
fout=open('C:/Users/HP/Desktop/foff.txt','w')
t1=finn.readline()
k1=int(t1)
for j in range(0, k1):
    cnt=0
    a,b=map(int,finn.readline().split())
    i=a
    p=i
    while i<=b:
        st=str(i)
        if(st==st[::-1]):
            i2=math.sqrt(i)
            if(i2==int(i2)):
                st=str(int(i2))
                if(st==st[::-1]):
                    fout.write(str(i)+' ')
        p=math.sqrt(i)
        p=int(p)
        label .upp
        p=p+1
        i=p*p
finn.close()
fout.close()
