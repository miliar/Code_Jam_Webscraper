inp = open('C-small-attempt1.in')
oup = open('C-small.out','w')
import math, sys
sys.stdout = oup
def isPalindrome(n):
    numDigs = int(math.ceil(math.log(n, 10)))
    def isPalindrome0(n, numDigs):
        if numDigs < 2:
            return True
        if n / (10 ** (numDigs - 1)) == n % 10:
            return isPalindrome0((n / 10) % 10** (numDigs - 2), numDigs - 2)
        else:
            return False
    return isPalindrome0(n, numDigs)

def genPalindromes(a, b):
    for n in range(a, b + 1):
        if isPalindrome(n):
            yield n
    
numCases = int(next(inp))
for case in range(numCases):
    print 'Case #' + str(case + 1) + ': ',
    s = 0
    a, b = [int(x) for x in next(inp).split()]
    print>> sys.stderr, int(math.ceil(math.sqrt(a))), int(math.sqrt(b))
    for num in genPalindromes(int(math.ceil(math.sqrt(a))), int(math.sqrt(b))):
        print >> sys.stderr, isPalindrome(num ** 2), num ** 2
        if num <= b and isPalindrome(num ** 2):
            s += 1
    print s
oup.close()
