#!/usr/bin/python

import os
import sys

def convert_to_nums(seq):
    return [1  if e is '+' else 0 for e in list(seq)]

def reduced_list(tmp):
    """ Return list with 1s removed"""
    print tmp

    for x in range(0, len(tmp)):
        if tmp[x] == 0:
            return tmp[x:]
    return []

def flip_list(l, k):
    
    print "List to be flipped"
    print l

    if k > len(l):
        return None

    for x in range(0, k):
        print l[x]
        if l[x] == 0:
            l[x] = 1
        else:
            l[x] = 0
        print l[x]

    return l   


def find_splits(l, k):  
    """ Return number of splits required"""
    count = 0
    reduced = l

    while True:
        reduced = reduced_list(reduced)
        print "After reducing " 
        print reduced

        if len(reduced) == 0:
            return count

        reduced = flip_list(reduced, k)
        print "After flipping " 
        print reduced

        if reduced is None:
            return "IMPOSSIBLE"

        count = count + 1        


def main():
    test_file = "test-pancakes"
    with open(test_file) as f:
        rows = f.read().splitlines()
    T = rows[0]
    cases = rows[1:]

    g = open('pancakes.out', 'w')

    # Run for each case
    for x in range(0,int(T)):
    
        N, K = cases[x].split()
        K = int(K)
    
        N = convert_to_nums(N)
        print N, K

        ans = find_splits(N, K)    
        
        g.write("Case #{}: {}\n".format(x+ 1, ans))

if __name__ == "__main__":
    main()
