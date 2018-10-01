import sys
import math

def check_palindrome(v):

    s = str(v)
    rp = len(s)/2
    lp = rp if len(s) % 2 else rp - 1

    while lp >= 0:
        if s[lp] != s[rp]:
            return False
        else:
            lp -= 1
            rp += 1
    else:
        return True


def fair_and_square(A, B):

    count = 0

    for i in range(int(math.ceil(math.sqrt(A))), int(math.sqrt(B)) + 1):
        if check_palindrome(i) and check_palindrome(i*i):
            #print 'Found palindrome', i, i*i, 'between', A, B
            count += 1

    return count

if __name__ == '__main__':

    C = int(sys.stdin.readline().strip())

    for i in range(C):

        A, B = map(int, sys.stdin.readline().strip().split())
        print 'Case #%s: %s' % (i+1, fair_and_square(A, B))

