from __future__ import division
def read_mapped(func=lambda x:x):
    return map(func, raw_input().split(" "))
def read_array(N, func):
    l = []
    for i in xrange(N):
        l.append(func(raw_input()))
    return l
def read_int():
    return int(raw_input())
def read_str():
    return raw_input()
def read_float():
    return float(raw_input())

T = read_int()

for case in xrange(T):
    a, b, k = read_mapped(int)
    acc = 0
    for i in range(a):
        for j in range(b):
            if i&j<k: acc += 1
    print "Case #{}: {}".format(case+1, acc)
