#!/usr/bin/python

import math

def numDigits(x):
    return int(math.floor(math.log10(x)) + 1)

def makePalindromes(prefix, digits):
    results = []
    
    reverse = 0
    temp = prefix
    while temp > 0:
        reverse = (reverse * 10) + (temp % 10)
        temp /= 10
    
    if digits % 2 == 1:
        for center in range(10):
            results.append(prefix * (10**(digits/2+1)) +
                           center * (10**(digits/2)) +
                           reverse)
    else:
        results.append(prefix * (10**(digits/2)) + reverse)
    return results

def isPalindrome(x):
    reverse = 0
    temp = x
    while temp > 0:
        reverse = (reverse * 10) + (temp % 10)
        temp /= 10
    return x == reverse

def ComputeFairAndSquares(A, B):
    count = 0
    srcA = int(math.sqrt(A))
    srcB = int(math.sqrt(B)) + 1
    
    numDigitsSrcA = numDigits(srcA)
    numDigitsSrcB = numDigits(srcB)
    
    prefixLow  = srcA / 10**(numDigitsSrcA / 2)
    prefixHigh = srcB / 10**(numDigitsSrcB / 2)
    
#    print prefixLow
#    print prefixHigh
    
    for dig in range(numDigitsSrcA, numDigitsSrcB + 1):
#    for dig in range(numDigits(A), numDigits(B) + 1):
        
        prefixBoundLow = prefixLow
        if dig == 1:
            prefixBoundLow = 0
        elif (dig > numDigitsSrcA):
            prefixBoundLow = 10**(dig/2 - 1)
            
        prefixBoundHigh = prefixHigh
        if dig == 1:
            prefixBoundHigh = 0
        elif (dig < numDigitsSrcB):
            prefixBoundHigh = 10**(dig/2)-1

#        print 'dig: ' + str(dig) + ' [' + str(prefixBoundLow) + ', ' + str(prefixBoundHigh) + ']'
        
#        for prefix in range(max(10**(dig/2), prefixLow), min(10**(dig/2+1)-1, prefixHigh) + 1):
        for prefix in range(prefixBoundLow, prefixBoundHigh + 1):
#            print dig, prefix, prefixBoundLow, prefixBoundHigh
            palins = makePalindromes(prefix, dig) # evens simple, odds x 10
#            print palins
            for p in palins:
                square = p * p
                if square >= A and square <= B and isPalindrome(square):
#                    print 'found', p, square
                    count += 1
    
    return count

###########################

T = int(raw_input())
#T = 1
for case in range(T):
    [A, B] = map(int, raw_input().split())
    
#    A = 1
#    B = 4
    
    print 'Case #' + str(case+1) + ': ' + str(ComputeFairAndSquares(A, B))
