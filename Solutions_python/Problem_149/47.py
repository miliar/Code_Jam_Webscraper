#Template code developed by Brett Olsen (brett.olsen@gmail.com), 2013
#for the Google Code Jam programming contest

###############################################################################
# Imports go here
###############################################################################

#Do proper division
from __future__ import division

#For faster numerical analysis
import numpy as np

import sys

#Needed for the memoization decorator
import collections
import functools

###############################################################################
# Global variables (for caching, etc.) go here
###############################################################################

###############################################################################
# Decorators (taken from http://wiki.python.org/moin/PythonDecoratorLibrary)
###############################################################################

class memoize(object):
   """Decorator. Caches a function's return value each time it is called.
   If called later with the same arguments, the cached value is returned
   (not reevaluated).
   """
   def __init__(self, func):
      self.func = func
      self.cache = {}
   def __call__(self, *args):
      if not isinstance(args, collections.Hashable):
         # uncacheable. a list, for instance.
         # better to not cache than blow up.
         return self.func(*args)
      if args in self.cache:
         return self.cache[args]
      else:
         value = self.func(*args)
         self.cache[args] = value
         return value
   def __repr__(self):
      '''Return the function's docstring.'''
      return self.func.__doc__
   def __get__(self, obj, objtype):
      '''Support instance methods.'''
      return functools.partial(self.__call__, obj)

###############################################################################
# Functions
###############################################################################

def precalculate():
    """Perform any calculations that need to be performed before the main path
    (e.g., preparing lookup tables, etc.)
    
    N.B. Make sure you make any important variables global so that other
    functions can access them.
    """
    pass

def read_input(infile):
    """This function should take an open input file, load in all of the
    relevant information for a single case of the problem, and output it
    as a single object.    
    """
    #Some utility functions to read in particular types of input
    def read_int():
        return int(infile.readline().strip())
    def read_ints():
        return np.array(infile.readline().split(), dtype=int)
    def read_bigints(): #For ints that won't fit directly in an int32 array
        line = infile.readline().split()
        return np.array(map(lambda x: int(x), line))
    def read_float():
        return float(infile.readline().strip())
    def read_floats():
        return np.array(infile.readline().split(), dtype=float)
    def read_string():
        return infile.readline().strip()
    def read_strings():
        return np.array(infile.readline().split(), dtype=object) #N.B. general dtype
    
    N = read_int()
    values = read_ints()
    assert N == len(values)
    
    return values
    
#Borrowed inversion code from
#http://stackoverflow.com/questions/337664/counting-inversions-in-an-array
#(runs in N lg N)

def count_inversion(lst):
    return merge_count_inversion(lst)[1]

def merge_count_inversion(lst):
    if len(lst) <= 1:
        return lst, 0
    middle = int( len(lst) / 2 )
    left, a = merge_count_inversion(lst[:middle])
    right, b = merge_count_inversion(lst[middle:])
    result, c = merge_count_split_inversion(left, right)
    return result, (a + b + c)

def merge_count_split_inversion(left, right):
    result = []
    count = 0
    i, j = 0, 0
    left_len = len(left)
    while i < left_len and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += left_len - i
            j += 1
    result += left[i:]
    result += right[j:]
    return result, count

#Just test the inversion code with a simple N^2 version
def new_count_inversion(lst):
    count = 0
    n = len(lst)
    for i in range(n):
        for j in range(i+1, n):
            if lst[i] > lst[j]:
                count += 1
    return count   

def updown_min(values): 
    print values
    
    min_invert = None
    for i in range(len(values)):
        #peak_invert = abs(peakidx - i)
        #left, right = removed[:i], removed[i:]
        #total = peak_invert + count_inversion(left.tolist()) + count_inversion(right[::-1].tolist())
        #print peak_invert, total, left, right
        
        left, right = values[:i], values[i:]
        total = count_inversion(left.tolist()) + count_inversion(right[::-1].tolist())
        print total, left, right
        
        if min_invert is None:
            min_invert = total
        elif total < min_invert:
            min_invert = total
    return min_invert
    
    
def solve_case(values):
    #Map them to the smallest integers to make it easier to debug
    sortedvals = np.sort(values)
    mapping = {}
    for i in range(len(values)):
        mapping[sortedvals[i]] = i+1
    for i in range(len(values)):
        values[i] = mapping[values[i]]
    
    print values
    
    values = values.tolist()
    
    #Iteratively move each smallest number to the closest end of the array
    n = len(values)
    count = 0
    for i in range(n):
        val = i + 1
        #print values, val
        idx = np.where(np.array(values) == val)[0][0]
        count += min(idx, len(values) - idx - 1)
        values.pop(idx)
    
    return count

###############################################################################
# Main execution path
###############################################################################

if __name__ == "__main__":
    #Do any pre-calculations required
    precalculate()
    
    #Open up the input & output files based on the provided input file
    assert len(sys.argv) == 2 #only one argument
    assert sys.argv[1][-3:] == ".in" #input must end with .in
    infile = open("%s" % sys.argv[1], 'r')
    outfile = open("%s.out" % sys.argv[1][:-3], 'w')
    
    #Read in the number of cases (the first input line) to iterate through
    cases = int(infile.readline().strip('\n'))
    for i in range(cases):
        
        #Read in the input data for this case
        case = read_input(infile)
        
        #Solve the problem for this case
        output = solve_case(case)
        
        #Write out the output of this case
        outfile.write('Case #%i: %s\n' % (i+1, output))
        print 'Case #%i: %s\n' % (i+1, output)
    
    #Close files
    infile.close()
    outfile.close()
