#!/usr/bin/env python
# encoding: utf-8

import sys
import os
import re

def main():
    [L,D,N] = map(int,sys.stdin.readline().split())
    #print L,D,N
    words = []
    for i in range(0,D):
        words.append(sys.stdin.readline().rstrip("\n"))	
    #print words
    
    for case_no in range(1,N+1):
        matches=0
        # loop over all words, see if they match
        pattern = sys.stdin.readline().rstrip("\n").replace("(","[").replace(")","]")
        for w in words:
            if re.match(pattern,w):
                matches+=1
        print "Case #%i: %i" % (case_no,matches);

if __name__ == '__main__':
	main()

