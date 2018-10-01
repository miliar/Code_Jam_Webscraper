#!env python

import sys;
import math;

def main():
    line  = sys.stdin.readline()
    words = line[:-1].split(' ')
    T = int( words[0] )

    c = 0;
    while 1:
        c += 1
        if c > T :
            break

        line  = sys.stdin.readline()
        words = line[:-1].split(' ')
        A = int( words[0] )
        B = int( words[1] )

        print "Case #%d: %d" % (c,ans(A,B))

def ndigit(n):
    if n > 1:
        return int( math.log10(n) + 1)
    else:
        return 1

def getCandidates(ndigit):
    ret = [];

    if ndigit == 1:
        ret.append(1)
        ret.append(2)
        ret.append(3)
        return ret
    elif ndigit == 2:
        ret.append(11)
        ret.append(22)
        return ret

    if 2*int(ndigit/2) == ndigit :
        # even number
        # (2) (1)
        ret.append( 2*10**(ndigit-1) + 2 )
        ret.append( 1*10**(ndigit-1) + 1 )
        # (1,1) (1,1,1) (1,1,1,1)
        v = 1*10**(ndigit-1) + 1
        for i in range(1,ndigit/2):
            ret.append( v + 1*10**i + 1*10**(ndigit-1-i) )
            for j in range(i+1,ndigit/2):
                ret.append( v + 1*10**i + 1*10**(ndigit-1-i) 
                              + 1*10**j + 1*10**(ndigit-1-j) ) 
                for k in range(j+1,ndigit/2):
                    ret.append( v + 1*10**i + 1*10**(ndigit-1-i) 
                                  + 1*10**j + 1*10**(ndigit-1-j) 
                                  + 1*10**k + 1*10**(ndigit-1-k) ) 
    else:
        # odd number
        # (2) (1) (2,1)
        ret.append( 2*10**(ndigit-1) + 2 )
        ret.append( 1*10**(ndigit-1) + 1 )
        ret.append( 1*10**(ndigit-1) + 1 + 2*10**((ndigit-1)/2) )
        # (1,1) (1,1,1) (1,1,1,1) (1,1,1,1,1)
        v1 = 1*10**(ndigit-1) + 1
        v2 = 1*10**(ndigit-1) + 1 + 1*10**((ndigit-1)/2);
        for i in range(1,(ndigit-1)/2):
            ret.append( v1 + 1*10**i + 1*10**(ndigit-1-i) )
            ret.append( v2 + 1*10**i + 1*10**(ndigit-1-i) )
            for j in range(i+1,(ndigit+1)/2):
                ret.append( v1 + 1*10**i + 1*10**(ndigit-1-i) 
                               + 1*10**j + 1*10**(ndigit-1-j) ) 
                ret.append( v2 + 1*10**i + 1*10**(ndigit-1-i) 
                               + 1*10**j + 1*10**(ndigit-1-j) ) 
                for k in range(j+1,(ndigit+1)/2):
                    ret.append( v1 + 1*10**i + 1*10**(ndigit-1-i) 
                                   + 1*10**j + 1*10**(ndigit-1-j) 
                                   + 1*10**k + 1*10**(ndigit-1-k) ) 
                    ret.append( v2 + 1*10**i + 1*10**(ndigit-1-i) 
                                   + 1*10**j + 1*10**(ndigit-1-j) 
                                   + 1*10**k + 1*10**(ndigit-1-k) ) 


    return ret


def ans(A,B):
    sqrt_A = math.sqrt(A)
    sqrt_B = math.sqrt(B)

    # get number of digit of sqrt(A) and sqrt(B)
    ndigit_A = ndigit(sqrt_A)
    ndigit_B = ndigit(sqrt_B)

    ret = 0
    candidates = getCandidates(ndigit_A)
    for i in range(0,len(candidates)):
        if candidates[i] >= sqrt_A and candidates[i] <= sqrt_B:
            ret += 1

    if ndigit_A != ndigit_B:
        candidates = getCandidates(ndigit_B)
        for i in range(0,len(candidates)):
            if candidates[i] <= sqrt_B:
                ret += 1

    for i in range(ndigit_A+1,ndigit_B):
        candidates = getCandidates(i)
        ret += len(candidates)

    return ret


if __name__ == '__main__':
    main()

