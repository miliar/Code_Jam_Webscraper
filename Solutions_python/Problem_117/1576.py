#!/bin/python

import numpy as np
    
def ssolve(mm):
    mn= mm[:][:]
    mm = np.matrix(mm)
    ccoollss = np.array(mm.sum(axis=0))
    rroowwss = np.array(mm.sum(axis=1))
    
    rows = len(mn)
    cols = len(mn[0])
    for i, row in enumerate(mn):
        for j, col in enumerate(mn[i]):
            if (mn[i][j] == 1):
                #print i,j
                if (rroowwss[i][0] != cols) and (ccoollss[0][j] != rows):
                    return False
    return True
        
        
def solve(num, text, oo):
    m = []
    mm = []
    a = text[:len(text)-1].split('\n')
    m.extend([item for item in a])
    for item in m:
        tmp = item.split()
        tmpint = [int(n) for n in tmp if n.strip()]
        mm.extend([tmpint])
    #if ssolve([[1,2,1]]):
    if ssolve(mm):
        out="Case #%s: YES\n"%(num)
    else:
        out="Case #%s: NO\n"%(num)
    oo.write(out)

    
if __name__ == '__main__':
    ff = open("B-small-attempt4.in")
    oo = open('output.txt', 'w')
    total = long(0)
    allText = ff.readlines()
    ff.close()
    
    total = int(allText[0])
    curr   = 2
    offset = int(allText[1].split()[0])

    for x in range(total):
        end = curr + offset
        #print curr, offset, end
        #print allText[curr:end]
        problem = ''.join(allText[curr:end])
        
        solve (x+1, problem, oo)
        
        curr = end
        if x == total -1:
            break
        offset = int(allText[curr].split()[0])
        curr += 1
    oo.close()
    