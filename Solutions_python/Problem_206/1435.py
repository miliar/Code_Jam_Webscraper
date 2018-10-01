f = open('one.in', 'r+')
from decimal import *
getcontext().prec = 7
open('one.txt', 'w').close()
n = open('one.txt', 'r+')
hh = []
l =  int(f.readline())
ds = []
hs = []
ns = []
for p in range (l):
    line = f.readline().split(" ")
    ds.append(int(line[0]))
    nn = int(line[1])
    cu = []
    for b in range(nn):
        line = f.readline()
        cu.append([int(line.split(" ")[0]), int(line.split(" ")[1])])
    hs.append(cu)
print(ds)

def speed(hs, dist):
    time = float((dist-hs[0][0])/hs[0][1])
    for h in hs:
        if (dist-h[0])/h[1]>=time:
            time =(dist-h[0])/h[1]
    return time



for c in range(len(hs)):
    n.write("Case #" + str(c+1)+": "+'{0:.6f}'.format(ds[c]/speed(hs[c],ds[c]))+"\n")

n.close()
f.close()
