#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math

def main(argv=None):
    if len(argv)<1:
        print "Please specify input file"
        return 1
    fh = open(argv[0], 'rt')
    line = fh.readline().strip()
    T = int(line)
#    print T
    for i in range(T):
        num_range=fh.readline().strip().split(" ")
        start_num=long(num_range[0])
        end_num=long(num_range[1])
        if start_num>end_num:
	    continue
#	print "num start %d end %d"%(start_num,end_num)
        sqrt_start=long(math.ceil(math.sqrt(start_num)))
        sqrt_end=long(math.floor(math.sqrt(end_num)))
#        print "sqrt start %d end %d"%(sqrt_start,sqrt_end)
        total=0
	for num_digits in range(len(str(sqrt_start)),len(str(sqrt_end))+1):
#	    print "num_digits %d"%num_digits	    
	    total+=get_number(num_digits,sqrt_start,sqrt_end)
        print "Case #%d: %d"%((i+1),total)

    fh.close()

def get_number(num_digits, sqrt_start, sqrt_end):
    sub_total = 0
    k=num_digits/2
    if num_digits==1:
	range_start=""
	range_end=""
        for i in range(9):
	    palindrome_sqrt=i
            if palindrome_sqrt<sqrt_start:
                continue
            if palindrome_sqrt>sqrt_end:
                break
	    palindrome=long(math.pow(palindrome_sqrt,2))
            if is_palindrome(str(palindrome)):
#                print palindrome_sqrt, palindrome
                sub_total += 1
	return sub_total
    else:
        range_start=str(long(math.pow(10,k-1)))
        range_end="9"*(k+1)
#    print "range %s to %s"%(range_start,range_end)
    if num_digits%2==0:
	for i in range(long(range_start),long(range_end)):
	    palindrome_sqrt=long(str(i)+str(i)[::-1])
	    if palindrome_sqrt<sqrt_start:
		continue
	    if palindrome_sqrt>sqrt_end:
		break
	    palindrome=long(math.pow(palindrome_sqrt,2))
	    if is_palindrome(str(palindrome)):
#		print palindrome_sqrt, palindrome
		sub_total += 1

    if num_digits%2>0:
        for i in range(long(range_start),long(range_end)):
	    for j in range(9):
                palindrome_sqrt=long(str(i)+str(j)+str(i)[::-1])
                if palindrome_sqrt<sqrt_start:
                    continue
                if palindrome_sqrt>sqrt_end:
                    break
                palindrome=long(math.pow(palindrome_sqrt,2))
                if is_palindrome(str(palindrome)):
#                    print palindrome_sqrt, palindrome
                    sub_total += 1
    return sub_total

def is_palindrome(str):
#    print "checking %s"%str
    first_half=str[:len(str)/2][::-1]
    return str.endswith(first_half)    


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

