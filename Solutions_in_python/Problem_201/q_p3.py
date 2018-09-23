from collections import defaultdict

T = int(input().strip())

for t in range(1, T+1):
    N, K = map(int, input().strip().split(' '))
    sofar = 0
    target = 1
    amin = N
    amax = N
    gapsizes = {}
    gapsizes[N] = 1
    while sofar < K:
        if sofar + target <= K:
            gs = defaultdict(int)
            amax = N
            for k, v in gapsizes.items():
                l = int((k-1)/2)
                r = int(k/2)
                gs[l] += v
                gs[r] += v
                amin = min(amin, l)
                amax = min(amax, r)
        else:
            gskeysorted = sorted(gapsizes.keys(), reverse=True)
            left = K - sofar
            idx = 0
            amax = 0
            while left > 0:
                amin = int((gskeysorted[idx] - 1)/2)
                amax = int((gskeysorted[idx])/2)
                left -= gapsizes[gskeysorted[idx]]
                idx += 1
        sofar += target
        target *= 2
        gapsizes = gs
    
    
    print('Case #%d: %d %d' % (t, amax, amin))
    