#!/usr/bin/env python

def m(p,q):
    for i in xrange(len(p)):
        if p==''.join(q[i:]+q[:i]):
            return True
    return False

if __name__=='__main__':
    T=int(raw_input())
    for z in xrange(T):
        a,b=map(int,raw_input().split(' '))
        n=0
        l=dict()
        for i in xrange(a,b+1):
            w=True
            for qq in l.keys():
                if(m(str(i),qq)):
                    w=False
                    match=qq
            if w:
                l[str(i)]=1
            else:
                l[match]+=1
        for i in l.values():
            n+=(i*(i-1))/2
        print "Case #{0}: {1}".format(z+1,n)
    

