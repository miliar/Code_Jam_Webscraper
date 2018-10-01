#!/usr/bin/python

import sys

INPUT = sys.stdin
INPUT = open(sys.argv[1],'r')

def getline():
    return INPUT.readline()[:-1]

def trace(*strs):
    return
    print >> sys.stderr, '..',
    for str in strs:
        print >> sys.stderr, str,
    print >> sys.stderr

def next_after(digits):
    trace( 'digits:', digits )

    L = len(digits)
    for i in range(2, L+1):
        dset = digits[-i:]
        trace( 'consider last', i, ':', dset )
        # can we get a bigger number by rearranging
        # the last i digits?
        # (We've already established that we can't with a smaller i.
        # so we must change digit i.
        # change it to the least digit in dset that's > dset[0]
        candidates = [d for d in dset if d > dset[0] ]
        trace( 'candidates:', candidates )
        if len(candidates) == 0:
            continue

        n = min(candidates)
        trace('least:', n)

        # then make the rest of the set the least (by sorting asc)
        dset.remove(n)
        trace('rest:', dset)
        dset.sort()
        trace('rest sorted:', dset)

        return digits[0:-i] + [n] + dset

    # This must be highest for the base set + "this many" zeroes
    # So go for least for base set + one more zero.
    dset = digits[:]
    n = min( d for d in dset if d > '0' )
    trace( 'n:', n )
    dset.remove(n)
    trace('rest:', dset)
    dset.sort()
    trace('rest sorted:', dset)

    return [n] + ['0'] + dset


n_cases = int(getline())
trace(n_cases,'cases:')
for case_num in range(1,n_cases+1):
    trace()
    trace( 'Case #', case_num )

    digits = list(getline().strip())
    next = ''.join(next_after(digits))

    print 'Case #%d: %s' % (case_num, next)
    sys.stdout.flush()

assert INPUT.readline() == ''

# vim: sw=4 ts=4 expandtab
