import math
def parser():
    f=open('A-small-attempt0 (1).in','r')
    cases=int(f.readline())
    for i in range(cases):
        r,t=f.readline().split(' ')
        ans=rings(int(r),int(t))
        print 'Case #'+str((i+1))+': '+str(ans)

def rings(r,t):
    #a*(2r+2a-1)\le t
    #2a^2+a(2r-1)=1(a^2+(2r-1)/4)
    #2(a-(1-2r)/4))**2-(1-2r)**2/8
    #((t-())/2)**.5+()
    return int(math.floor(((t*1.0+(((1-2*r)**2)/8.0))/2)**.5+(1-2*r)/4.0))


parser()
