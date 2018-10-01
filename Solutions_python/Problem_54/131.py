import sys
import fractions


def apocalypse(events):
    
    events = list(set(events))
    events.sort()
    #print 'events', events
    diffs = []
    for i in range(len(events)-1):
        for j in range(i+1, len(events)):
            diff = events[j] - events[i]
        
        diffs.append(diff)
    
    #print 'diffs', diffs
    
    """
    inter_gcds = diffs[:]
    while len(inter_gcds) > 1:
        mid_gcds = inter_gcds[:]
        inter_gcds = []
        for i in range(len(mid_gcds)):
            for j in range(i+1, len(mid_gcds)):
                inter_gcds.append(fractions.gcd(mid_gcds[i], mid_gcds[j]))
    opt_gcd = inter_gcds[0]
    """
    
    opt_gcd = diffs.pop()
    while diffs:
        opt_gcd = fractions.gcd(opt_gcd, diffs.pop()) 
            
    #print 'opt_gcd', opt_gcd
    
    if (events[0] % opt_gcd) == 0:
        return 0
    else:
        return opt_gcd - (events[0] % opt_gcd) 


if __name__ == '__main__':
    C = int(sys.stdin.readline())
    for i in range(1, C+1):
        events = map(int, sys.stdin.readline().split())
        N = events.pop(0)
        
        print 'Case #%s: %s' %  (i, apocalypse(events))

