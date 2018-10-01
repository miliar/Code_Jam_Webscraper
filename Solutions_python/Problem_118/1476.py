#!/usr/bin/python
import sys
import math

def is_palindrome(a):
    s = str(a)
    for i in xrange(len(s) // 2):
        if (s[i] != s[-1-i]):
            return False

    return True

def is_fair(a):
    return is_palindrome(a)

def gen_fair_and_square(lower, upper):
    l = int(math.sqrt(lower))
    u = int(math.sqrt(upper))

    for num in xrange(l, u+1):
        if is_fair(num):
            square = num * num
            if (is_fair(square)) and square >= lower and square <= upper:
                yield square


if __name__ == "__main__":
    numExamples = int(sys.stdin.readline().strip())

    example = 1
    for line in sys.stdin:
        (lower, upper) = tuple(map(int, line.strip().split()))

        #print "=========="
        #print lower, upper
        total = 0
        for num in gen_fair_and_square(lower, upper):
            total += 1

        print "Case #{}: {}".format(example, total)
        example += 1

