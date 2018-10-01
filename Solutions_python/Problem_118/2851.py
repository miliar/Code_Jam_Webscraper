# Outputs the number of 'Fair and square' numbers in a given interval.

import string
import math

def get_square(n):
  return int(math.floor(math.sqrt(n)))

def is_square(n):
    s = get_square(n)
    if (math.pow(s,2) == n):
        #print n , ' is square: ' , s
        return True
    else:
        #print n , ' is not square ' , s
        return False

def is_palindrome(n):
    str_n = str(n)
    #print 'len num : ' , len(str_n)
    if (len(str_n) == 1):
        #print 'Single numbers are palindromes : ' , str_n
        return True
    pal_len = len(str_n) / 2
    #print 'length of palindrome ', str_n , ':' , pal_len

    for p in range(pal_len):
        left = p
        right = len(str_n) - (p + 1)
        if (str_n[left] != str_n[right]):
            return False
    return True

def read_input(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    cases = int(lines[0])
    for c in range(1, cases + 1):
        ranges = string.split(lines[c])
        start = int(ranges[0])
        end = int(ranges[1])
        n = 0
        for test in range(start, end + 1):
            #print '>> Evaluating ' , test
            case = int(test)
            if (is_square(case) and is_palindrome(case) and is_palindrome(get_square(case))):
                #print test , ' is a palindrome'
                n = n + 1
            
        print 'Case #{0}: {1}'.format(c, n)

read_input('C-small-attempt0.in')