#!/usr/bin/env python

##Qualification Round
##Problem 1
##sellers
##Public Domain

import sys,os,fileinput,math

class Bot:
    def __init__(self,steps):
        self.place = 1
        self.orders = steps
        if len(steps)!=0:
            self.current = self.orders.pop(0)
        else:
            self.current = 1
    def walk(self):
        if self.place != self.current:
            if self.current<self.place:
                self.place -=1
            else:
                self.place +=1

    def push(self):
        if self.place != self.current:
            if self.current<self.place:
                self.place -=1
            else:
                self.place +=1
            return False
        else:
            if len(self.orders) != 0:
                self.current = self.orders.pop(0)
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
    sys.stdout.write("Case #"+str(case)+": "+str(data)+'\n')

def solve_case(input,case):
    raw_orders = input.get_line().split(' ')
    num_orders = raw_orders.pop(0)
    combined = []
    blue=[]
    orange=[]
    while len(raw_orders) != 0:
        bot = raw_orders.pop(0)
        k = int(raw_orders.pop(0))
        if bot == 'B':
            blue.append(k)
        else:
            orange.append(k)
        combined.append((bot,k))

    b=Bot(blue)
    o=Bot(orange)

    i=0
    while len(combined) !=0:
        ord = combined.pop(0)
        if ord[0] == "B":
            p = b
            w = o
        else:
            p=o
            w=b
        pushed = False
        while not pushed:
            pushed = p.push()
            w.walk()
            i+=1

    output_case(case,i)

if __name__ == '__main__':
    input = Input()
    cases = input.get_int()

    for i in range(0,cases):
        solve_case(input,i+1)
