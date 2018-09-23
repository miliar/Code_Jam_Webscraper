#!/usr/bin/env python3

import sys, os, re
import numpy as np
import math
from collections import defaultdict

def log(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

stylepoint_dict = {
    b'.': 0,
    b'x': 1,
    b'+': 1,
    b'o': 2
}
def count_stylepoints(b):
    total = 0
    for l in b:
        for x in l:
            total += stylepoint_dict[x]

    #order: b[Y,X]
    for i in range(b.shape[0]):
        d = defaultdict(int)
        for j in range(b.shape[1]):
            d[b[i,j]] += 1
        d[b'.'] = 0
        if sum(d.values()) - d[b'+'] > 1:
            #log("+1")
            #print(d)
            return -1
    
    for i in range(b.shape[1]):
        d = defaultdict(int)
        for j in range(b.shape[0]):
            d[b[j,i]] += 1
        d[b'.'] = 0
        if sum(d.values()) - d[b'+'] > 1:
            #log("+2")
            return -1

    for x in range(b.shape[0]):
        y = 0
        d = defaultdict(int)
        while x < b.shape[0] and y < b.shape[1]:
            d[b[x,y]] += 1
            x += 1
            y += 1
        d[b'.'] = 0
        if sum(d.values()) - d[b'x'] > 1:
            return -1

    for y in range(1, b.shape[1]):
        x = 0
        d = defaultdict(int)
        while x < b.shape[0] and y < b.shape[1]:
            d[b[x,y]] += 1
            x += 1
            y += 1
        d[b'.'] = 0
        if sum(d.values()) - d[b'x'] > 1:
            return -1
    
    for x in range(b.shape[0]):
        y = b.shape[1]-1
        d = defaultdict(int)
        while x < b.shape[0] and y >= 0:
            d[b[x,y]] += 1
            x += 1
            y -= 1
        d[b'.'] = 0
        if sum(d.values()) - d[b'x'] > 1:
            return -1

    for y in range(0, b.shape[1]-1):
        x = 0
        d = defaultdict(int)
        while x < b.shape[0] and y >= 0:
            d[b[x,y]] += 1
            x += 1
            y -= 1
        d[b'.'] = 0
        if sum(d.values()) - d[b'x'] > 1:
            return -1
            
    return total

def getbest(b, level=0):
    orig_stylepoints = count_stylepoints(b)
    if orig_stylepoints == -1:
        return orig_stylepoints, []
    bestsp = orig_stylepoints
    bestmoves = []
    for i in range(b.shape[0]):
        for j in range(b.shape[1]):
            cand = []
            if b[i,j] == b'.':
                cand = [b'o', b'x', b'+']
            elif b[i,j] == b'+' or b[i,j] == b'x':
                cand = [b'o']
            for c in cand:
                #log("%strying %c %d %d" % ("  " * level, c.decode("ascii"), i+1, j+1))
                olditem = b[i,j]
                b[i,j] = c
                sp, newmoves = getbest(b, level=level+1)
                #sp = count_stylepoints(b)
                if sp > bestsp:
                    bestsp = sp
                    bestmoves = ["%c %d %d" % (c.decode("ascii"), i+1, j+1)] + newmoves
                b[i,j] = olditem
    return bestsp, bestmoves

def printboard(b):
    for l in b.T:
        for x in l:
            sys.stderr.write(x.decode("ascii")),
        sys.stderr.write("\n")

def main():
    T = int(input().strip())
    for t in range(1, T+1):
        N, M = [int(x) for x in input().strip().split(" ")]
        #b = [['.' for i in range(N)] for j in range(N)]
        b = np.zeros((N, N), dtype=(bytes, 1))
        b[:] = '.'
        bp = np.zeros((N, N), dtype=np.int)
        bx = np.zeros((N, N), dtype=np.int)

        bx[:] = 2*(N-1)
        
        for x in range(N):
            for y in range(N):
                bp[x, y] = min(min(x, N-1-x), min(y, N-1-y))*2 + N - 1

        USED = 1000000
        def find_minimum():
            minvalp = np.min(bp)
            minvalx = np.min(bx)
            if minvalp <= minvalx:
                minarr = bp
                typ = b'+'
                minval = minvalp
            else:
                minarr = bx
                typ = b'x'
                minval = minvalx
            idx_f = np.argmin(minarr)
            idx = np.unravel_index(idx_f, minarr.shape)
            return typ, idx, minval

        def add_entry(typ, idx):
            #print("adding %s: %s" % (typ, str(idx)))
            if ((b[idx] == b'x') and (typ == b'+')) or ((b[idx] == b'+') and (typ == b'x')):
                b[idx] = b'o'
            else:
                b[idx] = typ
            if typ == b'x' or typ == b'o':
                bx[idx] = USED
                for i in range(N):
                    bx[i, idx[1]] = USED
                    bx[idx[0], i] = USED

                for i in range(max(-idx[0], -idx[1]), min(N-idx[0], N-idx[1])):
                    #if bx[idx[0]+i, idx[1]+i] != USED:
                    #    bx[idx[0]+i, idx[1]+i] -= 1
                    pass
                    
                for i in range(max(-N+idx[0], -idx[1]), min(idx[0], N-1-idx[1])):
                    #if bx[idx[0]-i, idx[1]+i] != USED:
                    #    bx[idx[0]-i, idx[1]+i] -= 1
                    pass

            if typ == b'+' or typ == b'o':
                bp[idx] = USED
                for i in range(N):
                    #if bp[i, idx[1]] != USED:
                    #    bp[i, idx[1]] -= 1
                    #if bp[idx[0], i] != USED:
                    #    bp[idx[0], i] -= 1
                    pass

                i = 0
                while idx[0]+i > 0 and idx[1]+i > 0:
                    i -= 1
                while idx[0]+i < N and idx[1]+i < N:
                    bp[idx[0]+i, idx[1]+i] = USED
                    i += 1
                i = 0 
                while idx[0]+i > 0 and idx[1]-i < N-1:
                    i -= 1
                while idx[0]+i < N and idx[1]-i >= 0:
                    bp[idx[0]+i, idx[1]-i] = USED
                    i += 1
                #for i in range(max(-N+idx[0], -idx[1]), min(idx[0]+1, N-idx[1])):
                #    bp[idx[0]-i, idx[1]+i] = USED 
            #printb()


        def printb():
            print("b, bp, bx:")
            print(b)
            print(bp)
            print(bx)

        #print("start")
        #printb()

        for m in range(1, M+1):
            c, R, C = input().strip().split(" ")
            R, C = int(R)-1, int(C)-1
            add_entry(c.encode("ascii"), (R, C))
            #print("b, bp, bx after:")
            #printb()
            #break

        b_orig = b.copy()

        #sys.stderr.write("orig\n")
        #printboard(b)        

        typ, idx, minval = find_minimum()
        #maxiter = 10
        it = 0
        while minval < USED:
            add_entry(typ, idx)
            typ, idx, minval = find_minimum()
            it += 1

        #sys.stderr.write("modified\n")
        #printboard(b)
        
        addlist = []
        for x in range(N):
            for y in range(N):
                if b[x,y] != b_orig[x,y]:
                    addlist.append("%s %d %d" % (b[x,y].decode("ascii"), x+1, y+1))
                    
         
        stylepoints = count_stylepoints(b)
        #modelsadded = len(modellist)
        print("Case #{}: {} {}".format(t, stylepoints, len(addlist)))
        for m in addlist:
            print(m)

if __name__ == '__main__':
    main()
