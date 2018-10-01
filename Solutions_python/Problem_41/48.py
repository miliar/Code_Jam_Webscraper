#!python

import sys
from collections import defaultdict

def valid_perm(num, dict):
    n_d = defaultdict(int)
    for char in num:
        n_d[int(char)] += 1
    for i in xrange(1, 10):
        if n_d[i] != dict[i]:
            return False

    return True

def find_smallest(dict):
    num = ""
    for i in xrange(1, 10):
        j = dict[i]
        while j > 0:
            num += str(i)
            j -= 1

    return num

if len(sys.argv) != 2:
    print "Supply a filename."
    exit(-1)

fn = sys.argv[1]

fh = open(fn, 'r')

text = fh.read().split('\n')

num_cases = int(text[0])
text = text[1:]

for i in xrange(0, num_cases):
    num = text[i]
    dict = defaultdict(int)

    prev_digit = 10
    add_zero = True
    index = 0
    perm_index = 0
    for char in num:
        digit = int(char)
        dict[digit] += 1
        if digit > prev_digit:
            add_zero = False
            perm_index = index
            
        prev_digit = digit
        index += 1

    if add_zero:
        next_num = find_smallest(dict)
        new_num = next_num[0]
        for z in xrange(0, dict[0]+1):
            new_num += '0'
        new_num += next_num[1:]
        print "Case #%d: %s" % (i+1, new_num)
        continue

    next_num = num[:perm_index-1]
    rest = num[perm_index-1:]
    new_dict = defaultdict(int)

    for char in rest:
        new_dict[int(char)] += 1
    init = int(rest[0])
    for ni in xrange(init+1, 10):
        if new_dict[ni] > 0:
            new_base = ni
            break

    next_num += str(new_base)
    new_dict[new_base] -= 1
    for ds in xrange(0, 10):
        j = new_dict[ds]
        while j > 0:
            next_num += str(ds)
            j -= 1
        
    print "Case #%d: %s" % (i+1, next_num)

fh.close()
