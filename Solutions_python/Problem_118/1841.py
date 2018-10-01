from math import sqrt, floor, ceil

def is_palindrome(num):
    """
    (int) -> boolean

    Tests if the given number is a palindrome

    >>> is_palindrome(1)
    True

    >>> is_palindrome(2)
    True

    >>> is_palindrome(11)
    True

    >>> is_palindrome(12)
    False

    >>> is_palindrome(121)
    True

    >>> is_palindrome(223)
    False

    >>> is_palindrome(2244)
    False
    """
    s = str(num)

    for i in range(len(s) // 2):
        if (s[i] != s[len(s) - 1 - i]):
            return False

    return True

def sqrt_range(low, high):
    """
    (int, int) -> int, int

    Calculates the range of square roots of numbers within
    the given range.

    Precondition: low <= high

    >>> sqrt_range(1, 1)
    (1, 1)

    >>> sqrt_range(2, 3)
    Traceback (most recent call last):
        ...
    ValueError

    >>> sqrt_range(1, 4)
    (1, 2)

    >>> sqrt_range(10, 120)
    (4, 10)

    >>> sqrt_range(100, 1000)
    (10, 31)
    """
    lo = ceil(sqrt(low))
    hi = floor(sqrt(high))
    if (lo <= hi):
        return int(lo), int(hi)
    else:
        raise ValueError

def count_fair_and_square(low, high):
    """
    (int, int) -> int

    Returns the count of 'fair numbers' within the given range

    >>> count_fair_and_square(1, 4)
    2

    >>> count_fair_and_square(10, 120)
    0

    >>> count_fair_and_square(100, 1000)
    2
    """
    try:
        lo, hi = sqrt_range(low, high)
        count = 0
        for i in range(lo, hi + 1):
            if (not is_palindrome(i) or not is_palindrome(i ** 2)):
                continue
            count += 1
        return count
    except ValueError: # there's no square number within that range
        return 0


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    import sys
    try:
        fname = sys.argv[1]
        try:
            fin = open(fname, 'r')
            case_count = int(fin.readline())
            for c in range(case_count):
                a, b = map(lambda s: int(s), fin.readline().split(' '))
                print 'Case #' + str(c + 1) + ':', count_fair_and_square(a, b)
        except IOError:
            print "Cannot read input file"
    except IndexError:
        print "Please specify the name of input file"
