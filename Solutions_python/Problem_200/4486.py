#!/bin/env python

def isTidy(integer):
    a = int(integer)
    integer = str(a) # Remove left 0 if any...
    d = int(integer[0])
    for i, digit in enumerate(integer[1:]):
        if d > int(digit):
            return (False, i)
        d = int(digit) 
    return (True, 0)


def solve(integer):
    tidy = isTidy(integer)
    a = int(integer)
    integer = str(a) # Remove left 0 if any...
    if tidy[0]:
        return integer
    else:
        index = tidy[1]
        if int(integer[index]) == 1:
            return '9'*(len(integer) - 1)
        else:
            res = ''
            for digit in integer[:(index+1)]:
                if digit != integer[index]:
                    res = res + digit
                else: 
                    a = int(digit)
                    res = res + str(a-1)
            res = res + '9'*(len(integer) - (index + 1))
            return res


if __name__ == '__main__':
    TC = input()
    for case in xrange(1, TC+1):
        i = raw_input()
        print ("Case #{}: {}".format(case, solve(i)))

