#!/usr/bin/python

import sys, math
if len(sys.argv) != 2:
    print "Error!"
    print "Usage: python fairnsquare.py inputfile"
    
def palindrome(number):
    bakup = number
    reversed_list = []
    while number:
        reversed_list.append(number % 10)
        number = number // 10
    for i in reversed_list:
        number = number*10 + i
    if bakup == number:
        return True
    return False

def square_of_palindrome(number):
    square_rt = math.sqrt(number)
    int_square_rt = int(square_rt)
    if int_square_rt == square_rt:
        if palindrome(int_square_rt):
            return True
        return False
    return False

input_file = sys.argv[1]
try:
    with open(input_file,"r") as inpu, open("Outputfile.txt","w") as out:
        cases = int(inpu.readline())
        for i in range(cases):
            count = 0
            li = list(inpu.readline().split(" "))
            a = int(li[0])
            b = int(li[1]) + 1
            for j in range(a,b):
                if palindrome(j) and square_of_palindrome(j):
                    count += 1
            string = "Case #%d: %d\n" %(i+1,count)
            out.write(string)
except IOError:
    print "Unable to open file"
    