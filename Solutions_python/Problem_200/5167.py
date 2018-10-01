"""Tidy numbers"""

def isTidy(num):
    
    num = str(num)
    current = 0
    
    for digit in num:
        d = int(digit)
        if d < current:
            return False
        current = d
    return True
        


f_in = open('B-small-attempt0.in', 'r')
f_out = open('bout.dat', 'w')
T = int(f_in.readline())

test_case = 1
for testcase in range(T):
    N = int(f_in.readline())

    last_tidy = 1
    for num in range(1, N + 1):
        if isTidy(num): last_tidy = num

    print("Case #{0}: {1}".format(test_case, last_tidy), file = f_out)
    test_case += 1

#L = [129, 999, 7, 99999999999999999, 20, 321, 654, 999990]

#for item in L:
 #   print("{0} is tidy: {1}".format(item, isTidy(item)))
