from math import *

def combinations_with_replacement(iterable, r):
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)

# Find all palindromes in a range
def palindromes(lower, upper):
    min_len = len(str(lower))
    max_len = len(str(upper))

    P = []

    for length in range(min_len, max_len+1):
        P += [p for p in palindrome_helper(length) if p >= lower and p <= upper]

    return P

# Find all palindromes of a certain length
def palindrome_helper(length):
    if (length == 1):
        return range(10)
    len_first_half = int(ceil(length/2.0))
    len_second_half = length-len_first_half
    sequences = combinations_with_replacement(range(10), len_first_half)
    first_halves = ["".join([str(j) for j in i]) for i in sequences]
    P = [first_half+first_half[len_second_half-1::-1] for first_half in first_halves]
    return [int(p) for p in P]

def is_palindrome(num):
    return str(num) == str(num)[::-1]

f = open('C-small-attempt0.in')

num_test_cases = int(f.readline())

for test_case in range(num_test_cases):
    (A, B) = [int(i) for i in f.readline().split()]
    (a, b) = [int(ceil(sqrt(A))), int(sqrt(B))]

    P = palindromes(a,b)

    count = 0
    for p in P:
        if is_palindrome(p**2):
            count += 1

    print "Case #"+str(test_case+1)+":", count

f.close()
