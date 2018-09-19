from math import sqrt, ceil

def is_palindrome(n):
    m, l = 0, n
    while l > 0:
        l, d = divmod(l, 10)
        m = 10*m+d
    return m == n

T = int(input())
for t in range(T):
    A, B = map(int, input().split())
    count = 0
    for n in range(int(ceil(sqrt(A))), int(sqrt(B)) + 1):
        if is_palindrome(n) and is_palindrome(n**2):
            count += 1
    print('Case #%d: %d' % (t+1, count))
