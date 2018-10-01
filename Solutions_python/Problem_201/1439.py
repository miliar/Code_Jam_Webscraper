import math
import time
import multiprocessing
from boto.glacier import concurrent

import sortedcontainers


def bathroom(nb_s, nb_p):
    blocks = sortedcontainers.SortedListWithKey([(0, nb_s-1, nb_s)], key=lambda (s, e, l): (-l, s))
    min_d = -1
    max_d = -1
    for person in range(1, nb_p+1):
        (min_d, max_d) = add_new_person(blocks)
    return min_d, max_d


# Returns the min distance and max distance.
# The blocks list is updated, but remains sorted.
# A block is a tuple (start, stop, length)
def add_new_person(blocks):
    # print blocks
    (s, e, l) = blocks.pop(0)
    min_d = int(math.floor((l - 1) / 2.0))
    max_d = int(math.ceil((l - 1) / 2.0))
    if not min_d == 0:
        blocks.add((s, s+min_d-1, min_d))
    if not max_d == 0:
        blocks.add((e-max_d+1, e, max_d))
    return min_d, max_d


def new_thread(nb_s, nb_p, index, min_res_list, max_res_list):
    (min_ires, max_ires) = bathroom(nb_s, nb_p)
    min_res_list[int(index)-1] = min_ires
    max_res_list[int(index)-1] = max_ires

procs = []
t = int(raw_input())
min_results = multiprocessing.Array("i", range(t))
max_results = multiprocessing.Array("i", range(t))
for i in xrange(1, t + 1):
    nb_stalls, nb_people = [int(st) for st in raw_input().split(" ")]
    p = multiprocessing.Process(target=new_thread, args=(nb_stalls, nb_people, i, min_results, max_results,))
    procs.append(p)
    p.start()
    # (min_res, max_res) = bathroom(nb_stalls, nb_people)
    # print "Case #{}: {} {}".format(i, max_res, min_res)
for p in procs:
    p.join()
for i in range(t):
    min_res = min_results[i]
    max_res = max_results[i]
    print "Case #{}: {} {}".format(i+1, max_res, min_res)
