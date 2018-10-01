import re
import numpy
import gmpy2
import math
#import sys

#sys.setrecursionlimit(10000)

def Output(CaseN, Num):
    outputLine = "Case #"+str(CaseN)+": "+str(Num)
    fw.write(outputLine + "\n")


def NextBiggerPalindrome(Xdigits):
    # for 999 it will return 999!s   
    # convert to list
    Xdigits = [int(x) for x in Xdigits]
    print "InputX", Xdigits
    l = len(Xdigits)
    lhalf = int(math.ceil(l/2))
    Ydigits = [x for x in Xdigits]

    for i in xrange(lhalf):
        Ydigits[l-1-i] = Xdigits[i]

    for i in xrange(lhalf, l):
        if Ydigits[i] < Xdigits[i]:
            Ydigits[l-1-i] = Ydigits[i] = Ydigits[i] + 1
            break


    #for i in xrange(l/2, l):
    #    if Ydigits[i] < Xdigits[i]
    #X = gmpy2.mpz( ''.join([str(x) for x in Xdigits]) )
    #Y = gmpy2.mpz( ''.join([str(x) for x in Ydigits]) )

    print "NextBiggerX", Ydigits
    return ''.join([str(x) for x in Ydigits])

def NextPalindrome(Xdigits):
    Xdigits = [int(x) for x in Xdigits]
    # x is playndrome already    
    l = len(Xdigits)
    Found = False
    for i in xrange(l/2, -1, -1): # l == 5. loop: 2,1,0
        if Xdigits[i] < 9:
            Xdigits[l-i-1] = Xdigits[i] = Xdigits[i] + 1
            Found = True
            break
        else:
            Xdigits[l-i-1] = Xdigits[i] = 0
    if not Found:
        # we were given 99999 string
        Xdigits[0] = 1
        Xdigits.append(1)
    return ''.join([str(x) for x in Xdigits])

def IsPalindrome(X):
    Xdigits = gmpy2.digits(X)
    Ydigits = NextBiggerPalindrome(Xdigits)
    return Xdigits == Ydigits 

##################################

#f = open('C-small-practice.in', 'r')
f = open('C-small.in', 'r')
#f = open('C-large.in', 'r')
fw = open('C.out', 'w')
lines = f.readlines()
T = int( lines.pop(0) )



for i in xrange(T):
    print '----------', i+1
    FandSCount = 0
    A, B = map ( lambda x: gmpy2.mpz(x), lines.pop(0).split(' ') )
    (Asqrt, rem) = gmpy2.isqrt_rem(A)
    if rem > 0:
        Asqrt += 1
    #Adigits = [x for x in gmpy2.digits(A)]
    Xdigits = NextBiggerPalindrome(gmpy2.digits(Asqrt))
    X2 = gmpy2.mpz(Xdigits)**2
    while X2 <= B:
        #print X2
        FandSCount += IsPalindrome(X2)
        Xdigits = NextPalindrome(Xdigits)
        X2 = gmpy2.mpz(Xdigits)**2

    Output(i+1, FandSCount)

#print IsPalindrome(1234321