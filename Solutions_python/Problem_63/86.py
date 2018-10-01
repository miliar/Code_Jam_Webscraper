from m_util import *
import math

T = int(raw_input())

for c in range(1, T + 1):       
        L, P, C = map(int, raw_input().split())
                
        count = 0
        if(L*C < P):
            while L < P:
                L *= C*1.0
                P /= C*1.0
                count += 1
                #print L, P, count
            
            count = int(math.ceil(math.log(count * 2, 2)))
            
        print "Case #%d: %s" % (c, count)
    
