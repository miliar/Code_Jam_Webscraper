import math
import itertools
test = int(raw_input())

def value1(r,h):
    val = [r*r, 2*r*h]
    val.append(sum(val))
    return val

def get(value):
    cakes_value_radii_sorted = sorted(value, key=lambda k: k[0][0], reverse=True)
    seed = cakes_value_radii_sorted[0][1][2]
    seed += sum([j[1][1] for j in cakes_value_radii_sorted[1:]])
    return seed

for i in range(1,test+1):
    total, stack = map(int, raw_input().split(" "))
    cakes = [map(int,raw_input().split(" ")) for j in xrange(total)]
    cakes_value = [[j,value1(j[0],j[1])] for j in cakes]
    total_k_cakes = itertools.combinations(cakes_value, stack)
    seed = max([get(j) for j in list(total_k_cakes)])
    print "Case #{}: {}".format(i, repr(math.pi * seed))