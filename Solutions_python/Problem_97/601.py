'''
Created on Apr 14, 2012

@author: moatasem
'''
import  math
def getNumRecycle(n,A,B,h):
        c=0
        if(h.get(n)==None):
            x=list(str(n))
            for i in xrange(1,len(x)):
                t1="".join(x[0:i])
                t2="".join(x[i:len(x)])
                num=int(t2+t1)
                
               
                if((num>=A and num<=B) and num<>n and h.get(num)==None):
                    #print "(",str(n),",",str(num),")"
                    h[num]=0
                    c+=1
            
        if (c==0):
            return 0
        else :
            c+=1
            res=math.factorial(c)/(2*math.factorial(c-2))
            return res
    
    
f = open("c.in", "r")
n=int(f.readline().strip())
for k  in xrange(n):
    d=f.readline().strip()
    A,B=[int(i) for i in d.split(" ")]
    count=0
    h={}
    for j in range(A,B+1):
        count+= getNumRecycle(j,A,B,h)
    print 'Case #'+str((k+1))+": "+str(count)