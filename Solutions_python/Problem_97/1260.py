from gen import *
fl = open('C-small-attempt0.in','r')
case=int(fl.readline())
for j in range(case):
    z=fl.readline()
    z=z.strip()
    z=z.split()
    A=int(z[0])
    B=int(z[1])
    result= f(A,B)
    print "Case #%d:"%(j+1),result
        

