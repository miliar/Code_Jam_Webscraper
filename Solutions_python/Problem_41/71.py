#!/usr/bin/env python 
################################################################################

import sys
import os
import logging

#if (os.environ.get("DEBUG") != None):
#logging.basicConfig(level=logging.DEBUG)

def main():
    input = sys.stdin
    
    # T specifies the number of test cases
    T = int(input.readline())
    logging.info("T = %d", T)
    
    for i in range(T):
        N = int(input.readline())
        processTestCase(i + 1, N)


def toDigits(N):
    l = map(int, list(str(N)))
    return l

def addZero(digits_in):
    digits = digits_in[:]
    logging.info("addZero %s", digits_in)
    # At this point we have the largest number we can generate
    # without increasing the number of digits...so, we should add
    # a zero at this point.  The formula will be to 
    digits.sort()
    first = digits[0]
    digits[0] = 0
    digits = [first] + digits
    i = 0
    while (digits[i] == 0): i += 1
    if (i > 0):
        t = digits[i]
        digits[i] = digits[0]
        digits[0] = t
    return digits

def findNext(digits_in):
    digits = digits_in[:]
    length = len(digits)
    logging.info("digits = %s", digits)

    if (len(digits) < 2):
        return addZero(digits_in)

    pivot = len(digits_in) - 2
    
    logging.info("pivot = %s", pivot)

    logging.info("digits[pivot] = %s max(digits[pivot+1:length]) = %s", digits[pivot], max(digits[pivot+1:length]))
    while (pivot > 0 and digits[pivot] >= max(digits[pivot+1:length])):
        logging.info("digits[pivot] = %s max(digits[pivot+1:length]) = %s", digits[pivot], max(digits[pivot+1:length]))
        pivot -= 1
        logging.info("pivot = %s", pivot)

    if (pivot == 0 and digits[0] >= max(digits[1:length])):
        # At this point we have the largest number we can generate
        # without increasing the number of digits...so, we should add
        # a zero at this point.  The formula will be to 
        logging.info("BIGGEST ORDER...MUST ADD ZERO")
        return addZero(digits)

    logging.info("THERE IS A BIGGER NUMBER")

    high_order = digits[0:pivot + 1]
    low_order = digits[pivot + 1:length]

    logging.info("digits = %s %s", high_order, low_order)

    low_order.sort()

    logging.info("digits = %s %s", high_order, low_order)

    for i in range(len(low_order)):
        # Find the digit to swap
        if (low_order[i] > high_order[len(high_order) - 1]):
            t = low_order[i]
            low_order[i] = high_order[len(high_order) - 1]
            high_order[len(high_order) - 1] = t
            break

    logging.info("digits = %s %s", high_order, low_order)

    low_order.sort()

    logging.info("digits = %s %s", high_order, low_order)

    digits = high_order + low_order

    logging.info("digits = %s", digits)

    return digits

def processTestCase(index, N):
    digits = toDigits(N)
    logging.info("index=%d, N=%d, digits=%s", index, N, digits)

    # 1. start at the rightmost, and look for a rightmost digit that
    # is greater than a digit to the left of it

    # 2. when you find that digits, take the group of those leftmost
    # digits and look for the smallest...place it in the leftmost
    # position


    # are lexographically smallest

    digits = findNext(digits)

    if (digits[0] == 0):
        print "BAD FORMED NUMBER:", digits
        sys.exit(-1)

    if (int("".join(map(str, digits))) <= N):
        print "DIDN'T FIND A BIGGER NUMBER:", N, " -> ", digits
        sys.exit(-1)
    
#     i = N + 1
#     while (toDigits(N) != toDigits(i)): i += 1
    

    #print "      " + " " * len(str(index)) + "  " + str(N)
    print "Case #" + str(index) + ": " + "".join(map(str, digits))
    
main()
sys.exit(0)
