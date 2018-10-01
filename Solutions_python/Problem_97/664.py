"""
Code jam qualification question 1 
"""

import sys
import string
from collections import defaultdict

def load_tests(path):
    f = file(path)
    num_tests = int(f.readline())
    lines = f.readlines()
    assert num_tests == len(lines)
    tests = []    
    for test_line in lines:
        ints = [int(n) for n in test_line.split()]
        assert len(ints) == 2, ints
        tests.append(ints)
        
    return tests       

def get_digits(num):
    if 0<= num and num <= 9:
        return 1
    else:
        return 1 + get_digits(num / 10)

def get_recycled(num):
    # num of digits - 1 minus number of zeroes
    digits = get_digits(num)
    remainder = 10
    mult = 10 ** (digits - 1)
    
    last_num = num
    ret = [num]
    for i in xrange(digits - 1):
        new_num = num / remainder + (num % remainder) * mult
        if last_num % 10 != 0:
            ret.append(new_num)        
        last_num = new_num

        remainder *= 10
        mult /= 10

    return ret
        
def solve(n, m):
    numbers = set(range(n, m + 1))
    last_len = len(numbers)
    
    uniques = 0
    
    while len(numbers) > 0:
        num = numbers.pop()
        recycled = set(get_recycled(num))
        
        last_len = len(numbers)        
        numbers -= recycled
        # +1 for the original number
        recycled_num = 1 + last_len - len(numbers)
 
        uniques += recycled_num * (recycled_num - 1) / 2
        
        
        last_len = len(numbers)
    
    return uniques
    
def main():
    tests = load_tests(sys.argv[1])
    
    
    for test, test_num in zip(tests, range(1, len(tests) + 1)):
        print 'Case #%d:' % test_num, solve(*test)
        
if '__main__' == __name__:
    main()