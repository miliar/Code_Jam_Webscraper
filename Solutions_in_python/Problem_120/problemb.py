import sys
import math

sys.stdin=open("A.txt")
f=open("out1.txt",mode='a')
sys.stdout=f
t=int(sys.stdin.readline())
for i in range(t):
    r,paint=[int(x) for x in sys.stdin.readline().split()]
    count=0
    
    paint_req= ((2*r)+1)
    while(paint>=paint_req):
        paint=paint-paint_req
        count=count+1
        paint_req=(2*r)+1+(4*count)
    
        
    print("Case #"+str(i+1)+": "+str(count),end='\n',file=sys.stdout)

f.close()
