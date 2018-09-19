#!/usr/bin/env python

import gmpy
import sys
import bisect
import time
#import profile

#def gen_palindrometable(start, stop):
#    table = []
#    n = start
#    stop = stop
#    i = 0
#    
#    if(not is_palindrome_raw(n)):
#        n = nextPalindrome(n)
#    while n < stop:
#        n = nextPalindrome(n)
#        if(i % 100000 == 0):
#            i = 0
#            print n
#        i += 1
#    return table
#
#def gen_lookuptable(start, stop):
#    table = []
#    
#    n = start
#    
#    while n < stop:
#        if(is_palindrome(n) and is_square_palindrome_raw(n)):
#            table.append(n)
#            
#        n = next_palindrome(n)
#    
#    return table

def is_palindrome_raw(i):
    s = str(i)
    sr = s[::-1]
    if(s == sr):
        return True
    return False

def is_palindrome(i):
    idx = bisect.bisect_left(palindrome_table, i)
    if(idx >= palindrome_table_len):
        return False
    if(palindrome_table[idx] == i):
        return True
    return False

def next_palindrome(i):
    idx = bisect.bisect(palindrome_table, i)
    if(idx >= palindrome_table_len):
        return stop
    return palindrome_table[idx];

###########################################
def nextPalindrome(num):
    length=len(str(num))
    oddDigits=(length%2!=0)
    leftHalf=getLeftHalf(num)
    middle=getMiddle(num)
    if oddDigits:
        increment=pow(10, length/2)
        newNum=int(leftHalf+middle+leftHalf[::-1])
    else:
        increment=int(1.1*pow(10, length/2))
        newNum=int(leftHalf+leftHalf[::-1])
    if newNum>num:
        return newNum
    if middle!='9':
        return newNum+increment
    else:
        return nextPalindrome(roundUp(num))
 
def getLeftHalf(num):
    return str(num)[:len(str(num))/2]
 
def getMiddle(num):
    return str(num)[(len(str(num))-1)/2]
 
def roundUp(num):
    length=len(str(num))
    increment=pow(10,((length/2)+1))
    return ((num/increment)+1)*increment
###############################


def is_square_palindrome_raw(i):
    res = gmpy.sqrtrem(i)
    if(res[1] == 0):
        if(is_palindrome_raw(res[0])):
            return res[0];
    return False

start = 1
#stop = 1000000
stop = 100000000000000 #14
#stop = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 #100

#tstartpalin = time.time()
#palindrome_table = gen_palindrometable(start, stop)
#tendpalin = time.time()
#palindrome_table_len = len(palindrome_table)
#print 'palindrome done ' + str(palindrome_table_len)
#print 'time: ' + str(tendpalin - tstartpalin)
#
#tstartlookup = time.time()
#lookup_table = gen_lookuptable(start, stop)
#tendlookup = time.time()
#lookup_table_len = len(lookup_table)
#print 'lookup done ' + str(lookup_table_len)
#print 'time: ' + str(tendlookup - tstartlookup )
#
#print lookup_table

fout = open('data/C-large.table', 'w')

n = start
stop = stop
i = 0

if(not is_palindrome_raw(n)):
    n = nextPalindrome(n)
while n < stop:
    if(is_square_palindrome_raw(n)):
        fout.write(str(n) + '\n')
    n = nextPalindrome(n)
    
    if(i % 11117 == 0):
        i = 0
        print n
    i += 1

#for c in range(lookup_table_len):
#    fout.write(str(lookup_table[c]))
#    if(c < lookup_table_len - 1):
#        fout.write('\n')

fout.close()
