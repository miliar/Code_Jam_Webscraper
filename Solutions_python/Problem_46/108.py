from copy import copy
from bisect import bisect,insort

def xl(l):
    return xrange(len(l))

def isgood(inds):
    tm=[m[inds[i]] for i in xrange(l)]
    #print "new",l
    #print [i for i in xrange(l)]
    #print m,[max(j for j in xrange(l) if m[i][j])<=i for i in xrange(l)]
    #print [[j for j in xrange(l) if m[i][j]=="1"] for i in xrange(l)]
    return all(max([0]+[j for j in xrange(l) if tm[i][j]=="1"])<=i for i in xrange(l))

def isin(li,it):
    #return it in li
    b=bisect(li,it)-1
    if b==len(li): return False
    #print allperms[b]==it,allperms[b],it
    return allperms[b]==it

for case in range(input()):
    print "Case #"+str(case+1)+":",
    l=input()
    m=[list(raw_input()) for i in xrange(l)]
    inds=range(l)
    q=[(inds,0)]
    allperms=[inds]
    while len(q)>0:
        curinds,n=q.pop(0)
        #print curinds,n,len(q),case
        if isgood(curinds):
            print n
            #if case==16:
            #    print curinds,n,len(q),case
            #    exit(0)
            break
        for i in xrange(l-1):
            newm=copy(curinds)
            newm[i],newm[i+1]=newm[i+1],newm[i]
            if not isin(allperms,newm):
                insort(allperms,newm)
                #allperms.append(newm)
                q.append((newm,n+1))
