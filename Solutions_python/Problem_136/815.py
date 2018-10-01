fl=open('B-large.in','r+')
import sys
sys.setrecursionlimit(100000)
#fl=open('input.txt','r+')

t=int(fl.readline())

def calculate(c,f,x,curr=0.0,rt=2.0,time=0.0,depth=0):
    if depth>15000:
        return 999999.9999
    else:
        if time >= x/2.0:
            return time
        else:
            if curr>c:
                t=0.0
            else:
                t=(c-curr)/rt
            return min(time+(x-curr)/rt,calculate(c,f,x,curr+(rt*t)-c,rt+f,time+t,depth+1))


def calculate2(c,f,x):
    curr=0.0
    rt=2.0
    time=0.0
    depth=0
    t1=x/rt
    t2=0.0

    while depth <=100001 and t2+(x/rt) <= t1:
        if depth>0:
            t1=min(t1,t2+(x/rt))
        t=(c-curr)/rt
        rt+=f
        t2+=t
        depth+=1
    return t1

for case in xrange(t):
    c,f,x=(float(e) for e in fl.readline().split())
    mi=calculate2(c,f,x)
    print 'Case #%d: %.7f'%(case+1,mi)
