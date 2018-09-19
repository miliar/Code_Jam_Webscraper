import math

def is_panlindrome(n):
    sn = str(n)
    return sn == sn[::-1]

def is_square_palindrome(n):
    sqrt = math.sqrt(n)
    if sqrt.is_integer():
        sqrt_int = int(sqrt)
        return is_panlindrome(sqrt_int)
    else:
        return False

T = int(raw_input())
for tc in range(T):
    print "Case #%d: " %(int(tc)+1),
    A, B = map(int, raw_input().split())
    count = 0
    for num in range(A, B+1):
        if is_panlindrome(num) and is_square_palindrome(num):
            count += 1
    print count

