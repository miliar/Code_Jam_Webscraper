import sys
from collections import deque

infile = sys.stdin

def combine(elements, combs, opps):
    result = deque()
    for e in elements:
        result.append(e)
        if len(result)>=2:
            c = combs.get(result[-1]+result[-2])
            if c:
                result.pop()
                result.pop()
                result.append(c)
                
            uniques = set(result)
            if any(o[0] in uniques and o[1] in uniques for o in opps):
                result.clear()
    
    return result

T = int(infile.readline())
for i in xrange(T):
    tokens = infile.readline().split()
    
    C = int(tokens[0])
    combs = {}
    for c in tokens[1:C+1]:
        combs[c[0:2]] = c[2]
        combs[c[1]+c[0]] = c[2]
        
    D = int(tokens[C+1])
    opps = set(tokens[C+2:C+2+D])
    
    elements = tokens[-1]
    
    #print combs, opps, elements
    result = combine(elements, combs, opps)
    print("Case #%d: [%s]" % (i+1, ', '.join(result)))
        