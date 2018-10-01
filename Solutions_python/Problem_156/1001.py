#!/usr/bin/python
import math

filename = "./B-small-attempt8.in.txt"
#filename = "./i1"
case = 1

def eat (s, arr):
    if len(arr) <= 0:
        return (s, [])
    else:
        return run (s+1, [x-1 for x in arr if x-1 > 0])

def special (s, arr):
    if len(arr) <= 0:
        return (s, [])
    if arr[0] == 9:
        h = 6
    else:
        h = arr[0] /2
    return run (s+1, [h, arr[0] -h] + arr[1:])

def run(s, data):
    arr = sorted(data, reverse=True)
#    print arr
    if arr[0] <= 2:
        return (s+arr[0], [])
    else:
        t1 = eat(s, arr)
        t2 = special(s, arr)
        return t1 if t1[0] < t2[0] else t2

for (n, line) in enumerate(list(open(filename, 'rt'))[1:]):
    if n % 2 == 0:
        pass
    else:
        items = [int(x) for x in line.strip().split(" ")]
        t = run(0, items)
        print "Case #%d: %d" % (case, t[0])
        case += 1
