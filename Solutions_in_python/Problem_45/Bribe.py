import sys, math, random
from copy import copy
 
sys.setrecursionlimit(10000)

f = open('data/C-small-attempt3.in', 'r')
o = open('data/C-small-attempt3.out', 'w')

t = f.readline().strip();

cell_def = []

def min_f(x, y):
    if 0 > x or x > y:
        return y
    return x

def release(s, e, qs, qe, level):
    if qs == qe:
        # print str(level) + " " + str(s) + "-" + str(cell_def[qs]) + "-" + str(e) + " " + str((e-cell_def[qs])+(cell_def[qs]-s))
        return (e-cell_def[qs])+(cell_def[qs]-s)
    
    if not (e >= s and qe >= qs):
        return 0
    
    """
    if middle > qs and qe > middle and e > cell_def[middle] and cell_def[middle] > s:
        min = min_f(min, release(s, cell_def[middle]-1, qs, middle-1, level+1)+release(cell_def[middle]+1, e, middle+1, qe, level+1) + release(s, e, middle, middle, level+1))
    
    middle = qe
    if middle > qs and cell_def[middle] > s:
        min = release(s, cell_def[middle]-1, qs, middle-1, level+1)+release(s, e, middle, middle, level+1)
    
    middle = qs
    if qe > middle and e > cell_def[middle]:
        min = min_f(min, release(cell_def[middle]+1, e, middle+1, qe, level+1)+release(s, e, middle, middle, level+1))
    """
    
    min = -1
    for middle in range(qs,qe+1,1):
        min = min_f(min, release(s, cell_def[middle]-1, qs, middle-1, level+1)+release(cell_def[middle]+1, e, middle+1, qe, level+1) + release(s, e, middle, middle, level+1))
                
    return min

for i in range(int(t)):    
    pq = f.readline().strip().split(' ')

    p = int(pq[0])
    q = int(pq[1])
    
    cell_def_x = f.readline().strip().split(' ')
    cell_def = []
    
    for x in cell_def_x:
        cell_def.append(int(x))
    
    o.write("Case #" + str(i+1) + ": " + str(release(1, p, 0, q-1, 0)) + "\n")
    o.flush()
    
    