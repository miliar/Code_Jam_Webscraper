# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 16:17:10 2017

@author: ASUS
"""

FILENAME = 'B-large.in'

def tidy(n):
    
    nlist = []
    for char in n.strip():
        nlist.append(char)
    nondec = True
    
    for i in range(len(nlist) - 1):
        if nlist[i] > nlist[i+1]:
            firstindex = i
            nondec = False
            break
    if nondec == True:
        return n
        
    marker = False
    for i in range(firstindex):
        if nlist[firstindex-i] > nlist[firstindex-i-1]:
            marker = True
            m = int(nlist[firstindex-i])
            m = m - 1
            nlist[firstindex-i] = str(m)
            for j in range(firstindex - i + 1, len(nlist)):
                nlist[j] = '9'          
            n = ''.join(nlist)
            return n
    if marker == False:
        m = int(nlist[0])
        m = m - 1
        nlist[0] = str(m)
        for i in range(len(nlist) - 1):
            nlist[i+1] = '9'
        if m == 0:        
            del nlist[0]
        n = ''.join(nlist)
        return n
            
fr = open(FILENAME, 'r')
fw = open('outputBl.txt', 'w')
t = fr.readline()
t = int(t.strip())
cases = fr.readlines()
for i in range(t):
    k = tidy(cases[i]).strip()
    fw.write("Case #{}: {}\n".format(i+1, k))
fr.close()
fw.close()