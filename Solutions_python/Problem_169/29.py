VERBOSE = False

def solve(v,x,sources):
    non_target_sources = []
    
    total_flow = 0.0
    for rate,temp in sources:
        if temp == x:
            total_flow += rate
            if VERBOSE:print 'temp=%f, flow=%f' % (temp,rate)
        else:
            non_target_sources.append((rate,temp))

    sources = non_target_sources
    sources.sort(key=lambda (rate,temp): temp)
    
    while len(sources) > 1:
        rate0,temp0 = sources[0]
        rate1,temp1 = sources[-1]
        
        if rate0 == 0.0:
            sources.pop(0)
            continue
        
        if rate1 == 0.0:
            sources.pop(-1)
            continue
        
        if temp1 < x or temp0 > x:
            break
        if temp0 == temp1:
            break
        r0 = (temp1-x) / (temp1-temp0)
        r1 = (temp0-x) / (temp0-temp1)
        c0,c1 = rate0/r0, rate1/r1
        c = min(c0,c1)
        low_is_limiting = c0 < c1
        f0 = r0*c
        f1 = r1*c
        total_flow += f0+f1
        if VERBOSE:print 'low: temp=%f, flow=%f ; high: temp=%f, flow=%f' % (temp0,f0,temp1,f1)
        sources[0] = (rate0-f0,temp0)
        sources[-1] = (rate1-f1,temp1)
        if (low_is_limiting):
            sources.pop(0)
        else:
            sources.pop(-1)
        
    
    if total_flow == 0.0:
        return "IMPOSSIBLE"
    else:
        return str(1.0/total_flow * v)
        
    
        

n_cases = input()
for case in range(1,n_cases + 1):
    n,v,x = raw_input().split(' ')
    n = int(n)
    v = float(v)
    x = float(x)
    
    sources = [map(float,raw_input().split(' ')) for _ in range(n)]
    
    solution = solve(v,x,sources)
    print "Case #%d: %s" % (case,solution)