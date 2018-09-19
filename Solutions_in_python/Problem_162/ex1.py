from queue import *
from array import *

def reverse(a):
    return int(str(a)[::-1])

f = open('A-small-attempt1.in', 'r')
h = open('store.txt','r')
g = open('output.txt', 'w')

num = int(f.readline())
d = array('I',(0 for j in range(1000001)))
for k in range(1000001):
    d[k] = int(h.readline())
    
for i in range (num):
    N = int(f.readline())
    count = d[N]
    s = "Case #" + str(i+1) + ": " + str(count) + '\n'
    g.write(s)

f.close()
g.close()
h.close()
