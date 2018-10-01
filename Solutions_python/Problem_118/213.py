
import sys
import math
from collections import deque
from bisect import bisect_right, bisect_left

def main():
    limit = 10**100;
    numbers = square_and_palindromic(limit)
    
    cases = int(sys.stdin.readline())
    for cs in range(1, cases+1):
        A, B = [int(i) for i in sys.stdin.readline().split()]
        print "Case #{}: {}".format(cs, bisect_right(numbers, B) - bisect_left(numbers, A))

def is_palindromic(n):
    str_n = str(n)
    i , j = 0, len(str_n) - 1
    while i < j:
        if str_n[i] != str_n[j]: 
            return False
        i += 1 
        j -= 1

    return True;

def div2_ceil(n):
    return int(math.ceil(len(n) / 2.))
 
def square_and_palindromic(limit):
    palind = deque([1,2,3])
    palind_n_sqr = [1,4,9]
    
    while palind:
        cte = str(palind.popleft())
        for c in ['0', '1', '2']:
            candidate = cte[:div2_ceil(cte)] + c + cte[div2_ceil(cte):]
            candidate = int(candidate)
            sqr_candidate = candidate * candidate
            if sqr_candidate > limit:
                return palind_n_sqr
            elif is_palindromic(candidate) and is_palindromic(sqr_candidate):
                palind.append(candidate)
                palind_n_sqr.append(sqr_candidate) 
    return palind_n_sqr

if __name__ == '__main__':
    main()
