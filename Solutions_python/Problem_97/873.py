#!/usr/bin/env python
# encoding: utf-8

import sys
import re
from itertools import combinations

T = int(sys.stdin.readline())
splitter = re.compile(r"\w{1,1}")

def permuta(number):
    ans = []
    last = number[-1]
    ans.extend(last)
    ans.extend(number[:-1])
    return ans

for i in range(T):
    result = 0
    line = map(int,sys.stdin.readline().split())
    A = line[0]
    B = line[1]
    for n in range(A, B):
        m = "".join(permuta(splitter.findall(str(n))))
        m_int = int(m)
        while (m_int != n):
            if (m_int > n and m_int <= B):
                result+=1
            m = "".join(permuta(splitter.findall(m)))
            m_int = int(m)
    print 'Case #%d: %s ' % (i+1, result)
        
        
        
        
    
    