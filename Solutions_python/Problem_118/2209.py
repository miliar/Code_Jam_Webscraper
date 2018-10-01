from sys import argv
from math import sqrt

f = open(argv[1], "r")

t = int(f.readline())

def pallindrome(val):
    return True if val == int(str(val)[::-1]) else False

for s in range(t):
    nums = f.readline().split()
    num1 = int(nums[0])
    num2 = int(nums[1])

    loop1 = int(sqrt(num1))
    loop2 = int(sqrt(num2))

    count = 0

    for i in range(loop1, loop2 + 1):
        if pallindrome(i) and pallindrome(i*i) and i*i >= num1:
            count += 1

    print "Case #%d: %d" % (s+1, count)
