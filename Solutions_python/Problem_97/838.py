#!/usr/bin/env python

import sys
import string

fname=sys.argv[1]

i=open(fname,'r')
o=open(fname+'.out','w')

'''readline Split'''
def rls(i):
    out=map(int, string.split(i.readline()))
    return out[0] if len(out)==1 else out

'''Output Case#...'''
def wout(o, i, *args):
    out="Case #"+ str(i)+":"
    for arg in args:
        out+=" "+str(arg)
    out+="\n"
    o.write(out)

N=rls(i)

def memoize(fn):
    stored_results = {}

    def memoized(*args):
        try:
            # try to get the cached result
            return stored_results[args]
        except KeyError:
            # nothing was cached for those args. let's fix that.
            result = stored_results[args] = fn(*args)
            return result

    return memoized

#@memoize
def genValid(listDigit, numDigit):
    ret=[]
    if numDigit==1:
        return listDigit 
    for v in genValid(listDigit, numDigit-1):
        for d in listDigit:
            ret.append(d+v)
    return ret


def isRecycle(a,b):
    for i in range(len(a)):
        if a[i:]+a[:i]==b:
            return True
    return False

def recycleList(a):
    ret=[]
    for i in range(1,len(a)):
        ret.append(a[i:]+a[:i])
    return ret

def isValidValue(validDigits, value):
    for c in value:
        if c not in validDigits:
            return False
    return True


for x in range(N):
    used=[]
    a,b=string.split(i.readline())
    A,B=int(a),int(b)
    num_digit=len(b)
    maxDigit=b[0]
    minDigit=0 if len(a)<len(b) else a[0]

    maxD=int(maxDigit)
    minD=int(minDigit)
    
    digit=map(str,range(minD,maxD+1))
#    list=genValid(digit, num_digit)
    
    ret=0

    for lnum in range(A,B+1): 
        l=str(lnum)
        recycleds=recycleList(l)

        for r in recycleds:
            rnum=int(r)
            if rnum > lnum and A<=rnum<=B:
   #             print l, r
                ret+=1

#    for y in range(A,B+1):
#        if y<10:
#            continue
#        yStr=str(y)
#        if not isValidValue(digit,yStr):
#            continue



    wout(o, x+1, ret)
    

