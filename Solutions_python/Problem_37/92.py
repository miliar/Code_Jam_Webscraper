#!/usr/bin/python
import sys

def ReadInts():
    return map(int, sys.stdin.readline().strip().split())


def ishappy(num_s, base):
    loopset=set()
    while True:
        # print "call sum_of_squares", num_s
        loopset.add(num_s)
        num_s = sum_of_squares(num_s, base)
        if num_s in loopset:
            break
    if num_s == "1":
        return True
    return False

def sum_of_squares(num_s, base):
    sum = 0
    for i in num_s:
        sum += int(i)*int(i)
    return convert_to_base(sum, base)

def convert_to_base(num, base):
    a=""
    while num > 0:
        a = str(num % base) + a
        num = num / base
    return a

def all_happy(num, bases):
    flag = True
    for base in bases:
        if not ishappy(convert_to_base(num, base), base):
            flag = False
            break
    return flag

def first_happy(bases):
    i = 1
    while True:
        i+=1
        # print i
        if all_happy(i, bases):
            return i
        
    
num = ReadInts()[0]

for i in xrange(1, num+1):
    print "Case #%d: %d" % (i, first_happy(ReadInts()))
    
    
