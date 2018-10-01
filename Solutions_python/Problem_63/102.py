#! /usr/bin/env python
import sys

from math import ceil,log

# parsing input for a case

def read_line_int(f):
    line = f.readline()
    arr = line.split()
    t = [int(i) for i in arr]
    return t

   

     
# to have a nice name
def getfilename():
    args = sys.argv
    n = len(args)
    if n>1:
        return args[1]




def info(f):
    t2 = read_line_int(f)
    L = t2[0]
    P = t2[1]
    C = t2[2]
    #print "donnees : %d\t%d\t%d\t"%(L,P,C)
    return L,P,C


def iter(L,P,C,k):
    if(L*C >= P):
        return k
    else:
        n = int(ceil(log(P/L,C)/2))
        #print "exposant %d"%n
        D = L * pow(C,n) 
        #print "nouvelle borne %d"%D
        a = iter(L,D,C,k+1)
        b = iter(D,P,C,k+1)
        return max (a,b)

def caseprocess(f,i):
    L,P,C = info(f)
    res = iter(L,P,C,0)
    return "Case #%d: %d\n" % (i+1,res)


# main
if __name__=='__main__':
    input = getfilename()
    name = input[:-3]
    output = name+".out"
    f = open(input,'r')
    t1 = read_line_int(f)
    T = t1[0]
    #print "nb of cases :%d\n" % T
    o = open(output,'w')
    for i in range(T):
        #print "case number %d processed\n" % i
        oline = caseprocess(f,i)
        #print oline
        o.write(oline)
    o.close()
    f.close()
