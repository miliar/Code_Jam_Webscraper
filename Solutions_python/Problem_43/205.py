
# -*- coding: cp949 -*-

import sys, copy

def get_base(str):
    base = 1
    l = list(str)
    for i in range(1, len(l)):
        if(l[i] not in l[:i]): base = base+1
    return base

global minv, table
def get_min(l, base, start, cur):
    global minv, table
    if(cur == len(l)):
        ex = len(l)-1
        v = 0
        for i in range(len(l)):
            v = v+int(table[l[i]])*int(base)**ex
            ex = ex - 1
        if(v < minv) : minv = v
    else:
        if(l[cur] not in table):
            for i in range(base):
                if(start == 1 and i == 0): continue
                if(i in table.values()): continue
                table[l[cur]] = i
                get_min(l, base, 0, cur+1)
                del table[l[cur]]
        else:
            get_min(l, base, 0, cur+1)
                
if(len(sys.argv) == 1):
    fin = open("ex1.in", 'r')
    fout = open("ex1.out", 'w')
else:
    fin = open(sys.argv[1], 'r')
    fout = open(sys.argv[2], 'w')

T = fin.readline().rstrip('\r\n')
T = int(T)

for i in range(T):
    global minv, table
    minv = 100000000000000000000
    table = {}
    l = fin.readline().rstrip('\r\n')
    base = get_base(l)
    if(base == 1): base = 2
    get_min(l, base, 1, 0)
#    g_cache = [[-1]*len(l) for i in range(len("welcome to code jam"))]
    fout.write("Case #%d: %d\n" % (i+1, minv))

fin.close()
fout.close()
