#! /usr/bin/python

import sys
import math

def isPalindrome(n):
    numstr = "%d" % n
    numstrlen = len(numstr)
    for idx in range((numstrlen/2)+1):
        if numstr[idx] != numstr[numstrlen-idx-1]:
            #print "%d is not palindrome" % n
            return False
    #print "%d is palindrome" % n
    return True


with sys.stdin as inp:
    numbertestcases = int(inp.readline())

    for case in range(numbertestcases):
        #print "Test case: %d" % (case+1)
        rangeline = inp.readline()[:-1].split(" ")
        #print rangeline
        rangestart = int(rangeline[0])
        rangeend = int(rangeline[1])

        sqrtstart = int(math.sqrt(rangestart))
        sqrtend = int(math.sqrt(rangeend))

        hitcount=0
        #print rangestart, rangeend, sqrtstart, sqrtend

        for chk in range(sqrtstart, sqrtend+1):
            #print "Check %d" % chk

            chksquare = chk*chk
            if (chksquare >= rangestart) and (chksquare <= rangeend):
                if isPalindrome(chk) and isPalindrome(chk*chk):
                    hitcount += 1
                    #print "%d and %d^2 (%d) are palindromes" %(chk, chk, chk*chk)

                
        print "Case #%d: %d" % (case+1, hitcount)

        #isPalindrome(12345)
        #isPalindrome(1)
        #isPalindrome(12)
        #isPalindrome(10)
        #isPalindrome(121)
        #isPalindrome(6677)
        #isPalindrome(6776)
        #isPalindrome(123456789087654321)
