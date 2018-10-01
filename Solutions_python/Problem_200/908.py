#!/usr/bin/env python 
def solve(number):
    digits=[int(d) for d in number[::-1]]
    # Read digits in reverse order, if a digit is smaller then the next one
    # reset to 9, and reduce the next 1 by 1
    for i in range(len(digits)-1):
        if digits[i]<digits[i+1]:
            # Set 9 to all digits 
            for i in range(0,i+1):
                digits[i]=9
            digits[i+1]=digits[i+1]-1
    return int(''.join([str(d) for d in digits[::-1]]))
if __name__ == "__main__":
    t = int(raw_input())
    for cas in xrange(1,t+1):
        ans = solve(*raw_input().split())
        print "Case #{}: {}".format(cas,ans)
