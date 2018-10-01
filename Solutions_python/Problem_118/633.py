import math
from bisect import *
lst = []
Sans = []

def palindrome(s):
    return s == s[::-1]

def test(n):
    if n == 0:
        return True

    if palindrome(str(n*n)):
        Sans.append(n)
        return True
    return False

def dfs(dep):
    if dep >= 30:
        return 

    for i in xrange(10):
        lst.append(str(i))

        s = ''.join(lst)
        a = test(int(s + s[-2::-1]))
        b = test(int(s + s[::-1]))

        if a or b:
            dfs(dep+1)

        lst.pop()

        if not a and not b:
            break

dfs(0)
Sans.sort()

T = int(raw_input())
for z in xrange(T):
    a, b = map(int, raw_input().split())

    a, b = int(math.ceil(a ** 0.5)), int(math.floor(b ** 0.5))
    
    l, r = bisect_left(Sans, a), bisect_right(Sans, b)
    
    ans = r - l
    #ans = sum( a <= k <= b for k in Sans )

    print 'Case #%d: %d' % (z+1, ans)
