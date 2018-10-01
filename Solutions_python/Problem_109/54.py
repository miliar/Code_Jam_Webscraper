import math
N = W = L = 0
radii = []
pos = []
def dist(a,b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
def isOK():
    for i in xrange(N):
        for j in xrange(i+1,N):
            if (dist(pos[i],pos[j])<radii[i]+radii[j]):
                return False
    return True;
    

from random import *
T = int(raw_input());
for t in xrange(T):
    s = "Case #"+str(t+1)+":"
    print s,
    [N,W,L] = map(int, raw_input().split());
    radii = map(int, raw_input().split());

    seed(1);
    pos = [[randint(0,W),randint(0,L)] for i in radii]
    while (True):
        if (isOK()):
            for i in pos:
                print i[0],i[1],
            break
        pos = [[randint(0,W),randint(0,L)] for i in radii]        

    
    print
