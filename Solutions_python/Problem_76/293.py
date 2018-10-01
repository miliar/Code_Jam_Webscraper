#!/usr/bin/env python

##Qualification Round
##Problem 3
##sellers
##Public Domain

import sys,os,fileinput,math

class Binarial:
    def __init__(self,value):
        self.data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for i in range(int(math.floor(math.log(value,2))),-1,-1):
            if value-2**i >= 0:
                value -= 2**i
                self.data[i]=1

class BinarialSum:
    def __init__(self):
        self.data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    def add(self,binarial):
        for i in range(0,len(self.data)):
            self.data[i] += binarial.data[i]
    def check(self):
        for d in self.data:
            if d%2 != 0:
                return False
        return True


class Input:
    def __init__(self):
        if 'large.in' in os.listdir('.'):
            self.f = fileinput.input('large.in')
        elif 'small.in' in os.listdir('.'):
            self.f = fileinput.input('small.in')
        elif 'test.txt' in os.listdir('.'):
            self.f = fileinput.input('test.txt')

    def get_line(self):
        return self.f.next().strip('\n')

    def get_int(self):
        return int(self.get_line())

def output_case(case,data):
    sys.stdout.write("Case #"+str(case)+": ")
    sys.stdout.write(str(data))
    sys.stdout.write('\n')

def solve_case(input,case):
    input.get_line()
    arr = input.get_line().split(' ')
    candies = [int(x) for x in arr]
    candies.sort()
    bin = BinarialSum()
    for c in candies:
        bin.add(Binarial(c))
    if bin.check():
        candies.pop(0)
        output_case(case,sum(candies))
    else:
        output_case(case,"NO")
if __name__ == '__main__':
    input = Input()
    cases = input.get_int()
    for i in range(0,cases):
        solve_case(input,i+1)
