#! /usr/bin/env python

import sys


# the memoization table
MEM = {}
# the word
WORD = ''


def num_subseq_of(sub, ind=0):
    """Find the number of times sub appears in WORD[ind:]."""
    global MEM
    global WORD

    count = 0
    word = WORD[ind:]

    # for single char base case,
    if len(sub) == 1:
        return word.count(sub) # feeling memoization doesn't improve

    s = sub[0]
    for i in xrange(ind, len(WORD)):
        c = WORD[i]
        if c == s:
            try:
                count += MEM[(i, sub[1:])]
            except KeyError:    
                MEM[(i, sub[1:])] = num_subseq_of(sub[1:], i + 1)
                count += MEM[(i, sub[1:])]
    
    return count


def _trunc(num, max=4):
    repr = str(num)
    length = len(repr)

    if length < max:
        diff = max - length
        for i in xrange(diff):
            repr =  '0' + repr
    elif length > max:
        slice = length - max
        repr = repr[slice:]

    return repr


def main(argv):
    global MEM
    global WORD

    if len(argv) == 1:
        input = sys.stdin
    else:
        input = open(argv[1])

    firstline = input.readline()
    N = int(firstline)

    for i in xrange(N):
        WORD = input.readline()
        MEM = {}
        num = num_subseq_of('welcome to code jam')
        print 'Case #%d: %s' % ((i + 1), _trunc(num))

if __name__ == '__main__':
    sys.exit(main(sys.argv))
