import math
finn=open('C:/Users/HP/Desktop/input.txt','r')
fout=open('C:/Users/HP/Desktop/output.txt','w')
n=finn.readline()
n=int(n)
for j in range(0,n):
    r,t=map(int,finn.readline().split())
    a=2*r-1
    b=math.sqrt(a*a+8*t)
    k=(b-a)/4
    k=int(k)
    fout.write('Case #'+str(j+1)+': '+str(k)+'\n')
finn.close()
fout.close()
