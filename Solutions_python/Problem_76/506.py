# Google Code Jam 2011 qualifying round.
# Does order matter?
# 101
# 110
# 111
#----
# 100
# Oh, it's just parity of each bit position.
# If a bit position's parity is 1, there's no solution.
# Each partition must have equal parity for each position.
# Is there a small change needed to partition each time you add one candy?
# Only need to consider candies which share set bits.
# But if all bits are set, that's all candies, so doesn't help much.
# But could sort by number of set bits so work is easy by time size gets big.
# 1 2 3 4 5
# 001
# 010
# 011
# 100
# 101
# NO (bit 0)
# 3 5 6
# 100
# 101
# 010
# 101
# 110
# 5+6=11
# Maybe Patrick always gets only 1 candy?  Always the smallest?
# 001
# 010
# 111
# 100
# Can never add only one candy to partitionable total.  Bit positions
# of candies added must have 0 parity.  So they can all go to Sean.
# 1010
# 0110
# 1000
# 0100
# We could remove any sets found with 0 parity and give the to Patrick, until
# we were left with the smallest candy.
# This question is isomorphic to: can you remove any one item and have parities
# of bit positions equal?  Duh.

import sys
def process(bitcounts, candy):
    for bitpos in range(10):
        bitcounts[bitpos] += candy % 2
        candy /= 2        
def run():
    file = open(sys.argv[1])
    numCases = int(file.readline())
    for case in range(1, numCases+1):
        file.readline()         # Ignore size
        candies = map(int, file.readline().split())
        bitcounts = [0]*10      # Max candy is 1000
        for c in candies:
            process(bitcounts, c)
        if [b for b in bitcounts if b%2 == 1]:
            result = 'NO'
        else:
            result = sum(candies) - min(candies)
        print 'Case #{0}: {1}'.format(case, result)
run()
