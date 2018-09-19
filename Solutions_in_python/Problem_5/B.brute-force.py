from util import *

def f(_):
    N = input() # shake
    M = input() # cust
    custs = []
    for _ in range(M):
        l = raw_input().split()
        prefs = map(int,l)
        custs.append(dict(zip(prefs[1::2],prefs[2::2])))
    min = None
    min_n = None
    for n in range(2**N):
        for c in custs:
            for s,m in c.iteritems():
                if (n >> (s-1)) & 1 == m:
                    sat = True
                    break
            else:
                break
        else:
            # everyone happy
            num_malted = sum(((n >> b) & 1) for b in range(N))
            if min is None or min > num_malted:
                min = num_malted
                min_n = n
    if min is None:
        return 'IMPOSSIBLE'
    else:
        return ' '.join(map(str, (((min_n >> b) & 1) for b in range(N))))

drive(f)
