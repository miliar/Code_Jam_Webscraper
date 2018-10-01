#/usr/bin/env python2.7
"""Fair and Square"""
from __future__ import print_function

"""
Output:

<number of fair-and-square numbers in the interval>
"""

import sys
import math
import bisect

# DEBUG
def DEBUG(*args, **kwargs):
    #print(*args, **kwargs)
    pass


class RangeCollection(object):
    def __init__(self):
        self.ranges = []

    def add(self, range):
        # Ranges are kept sorted
        bisect.insort_left(self.ranges, range)
        
    def largest_range_within(self, a, b):
        largest = None

        # Find range that starts at >= a
        r = FSRange(a, b, 0)
        i = bisect.bisect_left(self.ranges, r)
        if i == len(self.ranges):
            DEBUG("No largest_range_within after this start ({})".format(a))
            return None

        # TODO: sort by size, then start
        candidate = self.ranges[i]
        if candidate.within(r):
            largest = candidate

        #while candidate.within(r):
        #    DEBUG("candidate: {}".format(candidate))
        #    if largest is None or len(candidate) > len(largest):
        #        largest = candidate
        #       DEBUG("is largest!")
        #   i += 1
        #   if i == len(self.ranges):
        #       break
        #   candidate = self.ranges[i]
        #DEBUG("largest is {}".format(largest))
        return largest

class FSRange(object):
    # Ranges are sorted by (start, -len).
    # That is:
    # - smaller starts first
    # - within a group of same starts, bigger ranges first.

    def __init__(self, start, end, count):
        self.start = start
        self.end = end
        self.count = count

    def __repr__(self):
        return "FSRange({}, {}, {})".format(self.start, self.end, self.count)
    def __str__(self):
        return "FSRange({}, {}, {})".format(self.start, self.end, self.count)

    def __len__(self):
        return self.end - self.start

    def __eq__(self, other):
        return (self.start, self.end) == (other.start, other.end)

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.start < other.start or (self.start == other.start and self.end > other.end)

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not (self <= other)

    def __ge__(self, other):
        return self > other or self == other

    def within(self, other):
        return self.start >= other.start and self.end <= other.end


def is_palindrome(s):
    l = len(s)
    for i in range(l//2):
        if s[i] != s[l-i-1]:
            return False
    return True

def count_in_range(start, end):
    DEBUG("count_in_range({}, {})".format(start, end))
    if end - start <= 0:
        return 0

    existing_range = all_ranges.largest_range_within(start, end)
    DEBUG("existing_range: {}".format(existing_range))

    count = 0
    if existing_range is None:
        this_count = 0
        for i in xrange(start, end):
            if is_palindrome(str(i)) and is_palindrome(str(i*i)):
                this_count += 1
        all_ranges.add(FSRange(start, end, this_count))
        DEBUG("adding FSRange({}, {}, {})".format(start, end, this_count))
        count += this_count

    else:
        # Before the existing range
        pre_existing = count_in_range(start, existing_range.start)
        count += pre_existing
        DEBUG(pre_existing, count)
        # The existing range's count
        count += existing_range.count
        DEBUG(existing_range.count, count)
        # After the existing range
        post_existing = count_in_range(existing_range.end, end)
        count += post_existing
        DEBUG(post_existing, count)

    return count

def decide(a, b):
    int_a = int(a)
    int_b = int(b)
    start = int(math.ceil(math.sqrt(int_a)))
    end = int(math.floor(math.sqrt(int_b))) + 1

    count = count_in_range(start, end)
    return count

all_ranges = RangeCollection()
def run(infile):
    f = open(infile)
    num = int(f.readline())
    for i in xrange(num):
        a, b = f.readline().split()
        print('Case #{count}: {}'.format(decide(a, b), count=i+1))


if __name__ == '__main__':
    run(sys.argv[1])
