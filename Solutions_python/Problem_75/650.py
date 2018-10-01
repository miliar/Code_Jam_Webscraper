# -*- coding: utf-8 -*-
#WA
from collections import defaultdict

def doit():
    ans = []
    
    line = raw_input().split()
    
    combine = defaultdict(lambda : defaultdict(lambda:None))
    opposite = defaultdict(lambda : defaultdict(lambda:None))
    
    index = 0
    
    C = int(line[index])
    index += 1
    
    for i in xrange(index, index + C):
        v = line[i]
        b1 = v[0]
        b2 = v[1]
        ne = v[2]
        
        combine[b1][b2] = ne
        combine[b2][b1] = ne
    index += C
    
    D = int(line[index])
    index += 1
    
    for i in xrange(index, index + D):
        v = line[i]
        b1 = v[0]
        b2 = v[1]
        
        opposite[b1][b2] = True
        opposite[b2][b1] = True
    index += D
    
#    N = int(line[index])
    index += 1
    input = list(reversed(list(line[index])))
    
    elements = {}
    
    while input:
        e = input.pop()
        
        elements[e] = elements.get(e, 0) + 1
        ans.append(e)
        
        if len(ans) == 1: continue
        
        ne = combine[ans[-1]][ans[-2]]
        if ne:
            b1 = ans.pop()
            b2 = ans.pop()
            
            elements[b1] = elements[b1] - 1
            elements[b2] = elements[b2] - 1
            
            ans.append(ne)
        else:
            last_element = ans[-1]
            for element, count in elements.iteritems():
                if count == 0: continue
                if opposite[last_element][element]:
                    ans[:] = []
                    elements.clear()
                    break
    return ans

T = input()

for t in xrange(1, T+1):
    ans = doit()
    print 'Case #%d: %s' % (t, str(ans).replace('\'', ''))