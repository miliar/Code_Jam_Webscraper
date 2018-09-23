# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 07:00:45 2017

@author: Bert
"""

#digits non decreasing order
#8
#123
#555
#224488 tidy

#given N
#what is the largest n such that n is tidy and n<=N

def is_tidy(digits):
    for i in range(len(digits)-1):
        if digits[i+1] < digits[i]:
            return False
    return True
    

def handle_case(N):
    digits = list(map(int,N))
    while not is_tidy(digits):
        #find highest digit, then take most left
        h = max(digits)
        pos = digits.index(h)
        digits[pos] -= 1
        for i in range(pos+1,len(digits)):
            digits[i] = 9
    
        i = 0
        #don't return leading zeroes
        while digits[i] == 0:
            i += 1
        digits = digits[i:]
    return "".join(map(str,digits))


def test(n):
    print(handle_case(n))

#test("21\n".strip()) #19
#test("998") #899
#test("123") #123
#test("132") #129
#test("1000") #999
#test("7") #7
#test("111111111111111110")
#with open("B-small.in") as fh, open("B-small.txt","w") as op:
with open("B-large.in") as fh, open("B-large.txt","w") as op:
#with open("B-Test.in") as fh, open("B-test-out.txt","w") as op:
        cases = int(fh.readline())
        x = 0
        for line in fh:
            x += 1
            N = line.strip()
            o = "Case #{}: {}".format(x,handle_case(N))
            print (o)
            op.write(o)
            op.write("\n")