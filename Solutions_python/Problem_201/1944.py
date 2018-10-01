#!/usr/bin/python

import math

def search_larger(indexes):
    max_size = 0
    index = 0
    for i, idx_size in enumerate(indexes):
        indexes, size = idx_size
        if max_size < size:
            max_size = size
            index = i 
    return index

def len_(s):
    if s % 2 == 0:
        return s/2 - 1
    else:
        return s/2

def split(pair_indexes):
    new_index = []
    bound_b = min(pair_indexes)
    bound_t = max(pair_indexes)
    size = bound_t - bound_b + 1
    new_size = len_(size)
    
    s = set([bound_b, bound_b+max(new_size-1,0)])
    new_index.append([list(s), max(new_size - 1,0)+1])

    s = set([bound_b +new_size+1, bound_t])
    new_index.append([list(s),abs(bound_t - bound_b - new_size - 1)+1])

    choosen = bound_b + new_size
    sol = [abs(bound_t - choosen), abs(choosen - bound_b)]
    sol_ = [max(sol), min(sol)]
    return new_index, sol_


def stalls(size, individues):
    indexes = [ [[0, size-1], size] ]
    sol = [0,0]
    if size == individues :
        return sol
    for i in range(individues):
        greater = search_larger(indexes)
        [index , interval_size] = indexes[greater]
        if interval_size == 1:
            return [0,0]
        indexes.remove([index, interval_size])
        new_indexes, sol = split(index)
        for new_index in new_indexes:
           indexes.insert(greater - 1, new_index)
           greater = greater + 1
    return sol

def stalls_easy(size, individues):
    places = int(math.ceil(float(size-1)/float(individues)))
    return stalls(places, 1)

if __name__ == "__main__":
    # print split ([0,9])
    t = int(input())
    for test in range(t):
        input_ = raw_input("")
        size, individues = str.split(input_, " ")
        sol = stalls(int(size), int(individues))
        print "CASE #{}: {} {}".format(test+1, sol[0], sol[1])