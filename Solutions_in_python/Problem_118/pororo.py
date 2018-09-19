
import sys
import math

def isPalindrome(num):
    s = str(num)
    for lp in range(0, len(s)/2):
        if s[lp] != s[-lp - 1]: return False
    return True

fa = open(sys.argv[1], 'rt')
data = fa.read().split()
fa.close()

N = int(data.pop(0))

for C in range(1, N + 1):
    R = 0
    x1 = int(data.pop(0))
    x2 = int(data.pop(0))

    subx1 = int(math.sqrt(x1)) - 1
    subx2 = int(math.sqrt(x2)) + 1 # 1 for the error correcton

    fair = 0
    x = subx1
    while x < subx2:
        if isPalindrome(x) == True and isPalindrome(x*x) == True and (x*x) >= x1 and (x*x) <= x2:
            R = R + 1
        x = x + 1

    print 'Case #%d: %d' % (C, R)




