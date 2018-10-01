#!/usr/bin/env python

def is_complete(grid):
    for row in grid:
        if '?' in row:
            return False
    return True

def expand_row(s):
    found_first = False
    last_c = ''
    new_s = ''
    for i in xrange(len(s)):
        if s[i] is '?':
            if found_first:
                new_s += last_c
        else:
            if not found_first:
                new_s = s[i] * (i+1)
            else:
                new_s += s[i]
            found_first = True
            last_c = s[i]
    return new_s

t = int(raw_input())
for i in xrange(1, t + 1):
    grid = []
    rows, cols = [int(s) for s in raw_input().split(" ")]
    for r in range(rows):
        row = raw_input()
        grid.append(row)
    
    new_grid = []
    found_first = False
    last_row = None
    for x in xrange(len(grid)):
        mod_i = expand_row(grid[x])
        if mod_i is '':
            if found_first:
                new_grid.append(last_row)
        else:
            if not found_first:
                temp = []
                temp.append(mod_i)
                new_grid.extend(temp * (x+1))
            else:
                new_grid.append(mod_i)
            found_first = True
            last_row = mod_i
            
    print "Case #{}:".format(i)
    for row in new_grid:
        print row
