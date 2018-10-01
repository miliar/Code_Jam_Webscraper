import sys
sys.stdin=open("tw.in",'r')
sys.stdout=open("C:/Users/Penguin/Desktop/OUT.txt",'w')
for ii in xrange(1,int(raw_input())+1):
    a,b=raw_input().split()
    b=list(b)
    b=map(int,b)
    a=int(a)+1
    co=0
    k=0
    for i in xrange(1,a):
        k+=b[i-1]
        if b[i]:
            co+=max(0,i-k)
            k+=max(0,i-k)
    print 'Case #%i: %i'%(ii,co)
sys.stdout.close()
    
