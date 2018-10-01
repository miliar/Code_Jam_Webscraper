#!/usr/bin/python

import sys
import os

def flip_chars(line):
    for i in range(len(line)):
        if line[i] == '+':
            line [i] = '-'
        elif line[i] == '-':
            line[i] = '+'
    return line

def calculate_min_flips(line, flipper_len):
    flips = 0
    plus_str = "".join('+' for i in range(flipper_len))
    minus_str = "".join('-' for i in range(flipper_len))
    length = len(line)
    exact_string = "".join('+' for i in range(length))
    exact_neg_string = "".join('-' for i in range(length))
    if (line == exact_string): # Total Positive case
        return str(flips)
    if (line == exact_neg_string and length%flipper_len == 0): # Total -ve case
        flips = length/flipper_len
        return str(flips)

    num_happy = line.count('+')
    num_flat = line.count('-')

    list_line = list(line)

    for i in range(length):
        if ((length - i) < flipper_len):
            break

        if list_line[i] == '+':
            continue
        #print "input_chunk: " + str(list_line[i:i+flipper_len])
        flipped_chunk = flip_chars(list_line[i:i+flipper_len])
        #print "flipped_chunk:" + str(flipped_chunk)

        for j in range(flipper_len):
            list_line[i+j] = flipped_chunk[j]
        #print list_line
        flips = flips + 1

    modified_str = "".join(list_line)
    if (modified_str == exact_string):
        return str(flips)
    return "IMPOSSIBLE"

def run():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        n, m = [str(s) for s in raw_input().split(" ")]
        output = calculate_min_flips(n, int(m))
        print "Case #" + str(i) + ": " + str(output)

if __name__ == '__main__':
    run()
