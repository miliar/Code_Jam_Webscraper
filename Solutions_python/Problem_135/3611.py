#!/usr/bin/env python
import sys

def determine_output(overlap):
    if len(overlap) == 1:
        return str(overlap[0])
    elif len(overlap) == 0:
        return "Volunteer cheated!"
    else:
        return "Bad magician!"

def process_grid(rows):
    chosen = int(rows[0])
    return [int(x) for x in rows[chosen].strip().split(' ')]

def process_file(filename):
    with open(filename, 'r') as input:
        lines = input.readlines()
        num_tests = int(lines[0])
        for i in xrange(num_tests):
            offset = 10*i
            first = process_grid(lines[offset+1:offset+6])
            second = process_grid(lines[offset+6:offset+11])
            overlap = list(set(first) & set(second))
            print('Case #%d: %s' % (i+1, determine_output(overlap)))
 
if __name__ == '__main__':
    if len(sys.argv) == 2:
        process_file(sys.argv[1])
