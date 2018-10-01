# Problema A

import math
import string
import decimal

#inizio corpo

f=open("input.txt","r")
o=open("output.txt","w")

numcasi=int(f.readline())

i=1
while i<=numcasi:
    s=f.readline()
    m=string.split(s)
    n=int(m[0])
    A=int(m[1])
    B=int(m[2])
    C=int(m[3])
    D=int(m[4])
    x0=int(m[5])
    y0=int(m[6])
    M=int(m[7])
    coord=[]
    coord.append([x0,y0])
    k=0
    while k<n:
        x0=(A*x0+B)%M
        y0=(C*y0+D)%M
        coord.append([x0,y0])
        k+=1
    a=0
    print coord
    cont=0
    while cont<n:
        cont2=cont+1
        while cont2<n:
            cont3=cont2+1
            while cont3<n:
                if (coord[cont][0]+coord[cont2][0]+coord[cont3][0])%3==0 and (coord[cont][1]+coord[cont2][1]+coord[cont3][1])%3==0:
                    a+=1
                cont3+=1
            cont2+=1
        cont+=1        
                    
    o.write("Case #%d: %d\n" % (i,a))
    i=i+1