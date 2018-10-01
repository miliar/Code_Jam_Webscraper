#/usr/bin/env python2.7
"""Consonants"""
from __future__ import print_function

"""
Output:

n (int) - the n-value of the name
"""

# - How does Python deal w/ strings of len(10**6)?
# - the problem says "*AT LEAST* n consecutive consonants".
#
# * Naive approach: generate all substrings, check all for n consecutive consonants
# * Better: check as you generate the substrings.
#   - start w/ substrings of len(n)
# * Traverse the full string once, find all occurrences (start indexes) of n consecutive consonants
#   - for n consecutive consonants at index i, there are (i+1) * (len(name) - (i+n-1) + 1) substrings that contain it.
#   - n can be big

import sys

DEBUG_ON = False
def DEBUG(*args, **kwargs):
    if DEBUG_ON:
        print(*args, **kwargs)

def is_consonant(c):
    return c not in 'aeiou'

def find_cc(name, n):
    # Returns a list of indexes of n consecutive consonantns
    # FIXME: must be cleverer on long strings
    len_name = len(name)
    indexes = []
    for i, c in enumerate(name):
        if i > len_name - n:
            break
        if not is_consonant(c):
            continue

        for j in xrange(n):
            if not is_consonant(name[i+j]):
                break
        else:
            indexes.append(i)
            DEBUG("Substr at {}: {}".format(i, name[i:i+n]))
    return indexes

def decide(name, n):
    DEBUG(name, n)
    indexes = find_cc(name, n)
    len_name = len(name)
    # FIXME: silly way of de-duplicating substrings
    substr_indexes = set()
    for i in indexes:
        #n_value += (i+1) * (len_name - (i+n) + 1)
        substr_indexes.update((start, i+n+end-1)
                              for start in xrange(i+1)
                              for end in xrange(len_name-(i+n)+1))
    # FIXME: comment this out :P
    DEBUG(len(substr_indexes), list(sorted(list(substr_indexes))))
    return len(substr_indexes)

def run(infile):
    f = open(infile)
    num = int(f.readline())
    for i in xrange(num):
        name, n = f.readline().split()
        print('Case #{count}: {}'.format(decide(name, int(n)), count=i+1))


if __name__ == '__main__':
    run(sys.argv[1])
