#!/usr/bin/python3

import sys, re

INPUT = sys.stdin
INPUT = open(sys.argv[1],'r')

def getline():
    return INPUT.readline()[:-1]

class Bunch:
    def __init__( self, **kwds ):
        self.__dict__ = kwds


pause_after_trace = False
def mtrace(*strs):
    return
    atrace(*strs)

def atrace(*strs):
    f = sys.stderr
    print('..', end=' ', file=f)
    for str in strs:
        print(str, end=' ', file=f)
    print(file=f)
    if pause_after_trace:
        response = raw_input('? ')
        if response == 'q':
            sys.exit(1)

def memoize(f):
    memos = {}
    def memoized_f( *args ):
        try:
            result = memos[args]
            mtrace(args, ": got result from memo")
        except KeyError:
            result = f(*args)
            mtrace(args, ": got result by calling")
            memos[args] = result
        return result
    return memoized_f

# ------------------------------------------------------------------------------

n_cases = int(getline())
mtrace(n_cases,'cases:')
for case_num in range(1,n_cases+1):
    mtrace()
    atrace( 'Case #', case_num )

    (R, C) = map(int, getline().split())

    cake = []
    for r in range(R):
        row = getline()
        assert len(row) == C
        mtrace(row)
        cake.append(row)
    mtrace()

    def is_blank(row):
        mo = re.search(r'[^?]', row)
        if mo is None:
            mtrace(row, 'is blank')
            return True
        else:
            mtrace(row, 'is not blank')
            return False

    def apportion_row(row):
        # Be greedy
        current_initial = re.search(r'([^?])', row).group(1)
        apportioned_row = ''
        for c in range(C):
            old_char = row[c]
            if old_char == '?':
                pass
            else:
                current_initial = old_char
            apportioned_row += current_initial
        mtrace(row, 'apportioned =>', apportioned_row)
        return apportioned_row

    # Find the first non-blank row
    for (r,row) in enumerate(cake):
        if not is_blank(row):
            fnbr = r
            fnb_row = row
            break
    else:
        assert 0, "some row must be non-blank!"

    # Decide how to apportion that row.
    new_row = apportion_row(fnb_row)

    # Go back and 'install' that row for previous blank lines
    for r in range(fnbr):
        cake[r] = new_row

    # Install it for this line:
    cake[fnbr] = new_row

    # And proceed
    for r in range(fnbr+1, R):
        row = cake[r]
        if is_blank(row):
            # Just repeat the previous row
            pass
        else:
            # Apportion this row and remember it.
            new_row = apportion_row(row)
        cake[r] = new_row

    print('Case #%d:' % case_num)
    for row in cake:
        print(row)

    sys.stdout.flush()

assert INPUT.readline() == ''

# vim: sw=4 ts=4 expandtab
