#!/usr/bin/env python
import math

def get_mm(n):
    if n < 1:
        return (0, 0)
    return (int(n/2), int((n-1)/2))

def do_it(i, j):
    a= math.pow(2, int(math.log(j, 2)))
    return get_mm((i-j%a)/a)	 

f = open('input', 'r')
o = open('output', 'w')

T = int(f.readline().strip())
ll = [i.split() for i in f.readlines()]
l = [[int(x), int(y)] for x, y in ll]

for c in range(T):
    res = do_it(l[c][0], l[c][1])
    o.write("Case #{}: {} {}\n".format(c+1, res[0], res[1]))
    
o.close()
f.close()
