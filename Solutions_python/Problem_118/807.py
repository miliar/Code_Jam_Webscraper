"""
Problem: 


This script was written for Python 3.3.
It
 * reads from standard input
 * writes to standard output
 * logs to standard error

@author: Eric Dong
"""

# Python built-in libraries
import itertools
import math
import sys
import logging

# Log to standard error
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG, \
                    format='%(asctime)s [%(levelname)-7s] %(message)s')

def main():
    
    mainmod = sys.modules['__main__']
    if mainmod and hasattr(mainmod, '__file__'):
        logging.info("Running {}".format(mainmod.__file__))

    cases = nextint()
    for case in range(1, cases+1):
        a, b = nextints()
        result = solve(a, b)
        print("Case #{}: {}".format(case, result))
    sys.stdin.close()

def reverse_i(x):
    return int(str[::-1])
    
def reverse_i(x, digits):
    return int(str(x)[::-1])

class Palindrome:
    def __init__(self, suffix, head, digits):
        self.suffix = suffix
        self.head = head
        self.digits = digits
        self.value = self.__value()
    
    def __value(self):
        result = 0
        for d in itertools.chain(self.suffix[:0:-1], self.suffix[self.head:]):
            result = result*10 + d
        return result
    
    def __feasible(self, q):
        return True
        # Sub-suffix to consider
        ss = self.suffix[q:]
        # Number of digits to consider
        d = len(ss)
        
        # y: Sub-suffix value
        y = 0
        for v in ss:
            y = y*10 + v
        
        # yy: Sub-suffix value, squared, right-most d digits
        yy = (y**2) % (10 ** d)
        
        # x: Reverse of sub-suffix
        x = reverse_i(y, d)
        xx1 = x**2
        sxx1 = str(xx1)
        nxx1 = len(sxx1)
        
        xx2 = (x+1)**2 - 1
        sxx2 = str(xx2)
        nxx2 = len(sxx2)
        
        assert 0 <= nxx2 - nxx1 <= 1
        
        logging.debug("y=%d, xx1=%d, xx2=%d, sxx1=%s, sxx2=%s", y, xx1, xx2, sxx1, sxx2)
        if nxx1 == nxx2:
            return int(sxx1[:d]) <= yy <= int(sxx2[:d])
        else:
            return int(sxx1[:d]) <= yy or yy <= int(sxx2[:d])
          
    def increment(self):
        q = None
        done = False
        while True:
            q = self.__increment(q)
            if q is None:
                break
            if self.__feasible(q):
                logging.debug("Feasible: q=%d", q)
                break
            else:
                logging.debug("Not feasible: q=%d", q)
        
        self.value = self.__value()
    
    def __increment(self, q=None):
        q = q or self.head
        onod = self.digits % 2
        suffix_len = len(self.suffix)
        overflow = False
        
        while q < suffix_len:
            if self.suffix[q] < 9:
                self.suffix[q] += 1
                break
            self.suffix[q] = 0
            q += 1
            overflow = True
            
        if not overflow:
            return q
        
        if q == suffix_len:
            # Need more digits
            self.digits += 1
            if onod:
                self.suffix.append(1)
                self.head = 1
            else:
                self.suffix[-1] = 1
                self.head = 0
                q = suffix_len - 1

        return q
    
    def __repr__(self):
        return "{{suffix: {}, head: {}, digits: {}, value: {}}}".format(self.suffix, self.head, self.digits, self.value)
        

def square_is_palindrome(j):
    k = j**2
    s = str(k)
    return s == s[::-1] 
    
def solve(a, b):
    
    # Work in the square-root space
    lower, upper = math.floor(math.sqrt(a)) - 1, math.ceil(math.sqrt(b)) + 1
    digits = len(str(lower))
    p = digits // 2
    onod = digits % 2
    suffix = [int(t) for t in str(lower)[-1-p::-1]]
    if not onod:
        suffix.insert(0, 0)
    matches = 0
    head = 0 if digits % 2 else 1
    
    logging.debug("a=%d, b=%d, lower=%d, upper=%d", a, b, lower, upper)
    palindrome = Palindrome(suffix, head, digits)
    while palindrome.value <= upper:
        logging.debug("Current palindrome: %s", palindrome)
        while palindrome.value**2 < a:
            palindrome.increment()
            logging.debug("Oops, too small: now %s", palindrome)
        if palindrome.value**2 > b:
            logging.debug("Exceeded: %s", palindrome)
            break
        
        if square_is_palindrome(palindrome.value):
            matches += 1
        palindrome.increment();
    
    return matches
        

##############################################################
# Utility functions
        
def nextstr():
    """
    Returns the next line from standard input,
    without any trailing newlines.
    """
    l = sys.stdin.readline()
    if l[-1] == '\n':
        l = l[:-1]
    return l
    
def nextint():
    """
    Returns the next line from standard input as an integer.
    """
    return int(nextstr())

def nextints():
    """
    Returns the next line from standard input as a list of integers,
    where the input is split by ' '.
    """
    return [int(t) for t in nextstr().split(' ')]
       
if __name__ == '__main__':
    main()