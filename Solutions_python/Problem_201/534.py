# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 00:54:44 2017

@author: Miguel
"""

import sys

def divideSpace(size):
    if size % 2 == 0: ## odd number
        return size / 2, (size / 2) - 1
    else:
        return size / 2, size / 2

def bathroomStall(n,k):
    empty_spaces = {n : 1}
    
    while k > 0:
        most_space = max(empty_spaces.keys(), key=int)
        n_spaces = empty_spaces[most_space]
        l, r = divideSpace(most_space)
       # print most_space, l, r
        if n_spaces >= k:
            return str(max(l,r)) + " " + str(min(l,r)) 
            #return l, r
        del empty_spaces[most_space]
        k = k - n_spaces
        if l not in empty_spaces:
            empty_spaces[l] = n_spaces
        else:
            empty_spaces[l] += n_spaces
        
        if r not in empty_spaces:
            empty_spaces[r] = n_spaces
        else:
            empty_spaces[r] += n_spaces
        

counter = 0

for line in sys.stdin:
    if counter == 0:
        counter += 1
        n_cases = int(line)
        continue
    line = line.split(" ")
    n = int(line[0])
    k = int(line[1])
    
    print "Case #" + str(counter) + ": " + str(bathroomStall(n, k))
    counter += 1