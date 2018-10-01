#!/usr/bin/env python
#
# Luke Southam <luke@devthe.com>
# GCJ Problem A. Magic Trick
#

# I/O stuff.
read_int  = lambda: int(raw_input())
read_line = lambda: raw_input().split()
read_ints = lambda *args: map(int, read_line())

# Lets start.
tests = read_int()

for test in range(1, tests+1):
    # Get inputs.
    row_a  = read_int()
    grid_a = map(read_ints, xrange(4))

    row_b  = read_int()
    grid_b = map(read_ints, xrange(4))
    
    # Find the selected rows.
    row_a = grid_a[row_a - 1]
    row_b = grid_b[row_b - 1]

    # Get the row differences.
    diff = filter(lambda i: i in row_b, row_a)

    # Choose accordingly.
    if len(diff) == 1:
        diff =  diff[0]
    elif len(diff) > 1:
        diff =  "Bad magician!"
    else:
        diff =  "Volunteer cheated!"

    # Output.
    print "Case #%i: %s" % (test, diff)

