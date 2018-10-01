import math
import string
import sys

count = 0
a= open("C-small-attempt1.in","r")
b=a.readline()
b2=int(b)
t=1;
def Palin(p):
    p1=str(p)
    #print p1[0]
    plen = len(p1)
    #print plen
    i=0
    j= plen-1
    flag=0
    while i<plen:
        if p1[i]!=p1[j]:
            flag=1
        i=i+1
        j=j-1
    if flag==0:
        return "True"
    else:
        return "False"
while t<=b2: 
    c=a.readline()
    d=c.split()
    i=int(d[0])
    j=int(d[1])
    while i<=j:
        w = int(i)
        if Palin(w)== "True":
            x = math.sqrt(i)
            z = int(x)
            y = x.is_integer()
            if y == True:
                if Palin(z) == "True":
                    count = count + 1
        i=i+1
    
    print "Case #",;sys.stdout.softspace=False;
    print t,;sys.stdout.softspace=False;
    print ":",
    print count
    count = 0
    t=t+1
    
sys.stdout.softspace=False;
a.close()

