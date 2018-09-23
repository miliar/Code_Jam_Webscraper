import collections

def last_lr(N, K):
    
    if K == N:
        return 0, 0
    
    d = collections.deque()
    
    d.append(N)
    
    for i in range(K):
        # process person i
        
        # n = top.popleft()
        
        n = d.popleft()
        
        # person i sees the longest contiguous set of empty stalls,
        #   which has n empty stalls
        # person i occupies the middle (or left middle) stall in that set
        #   leaving to their left,  l = (n-1)/2 empty stalls
        #       and to their right, r =     n/2 empty stalls
        
        l = (n-1)/2
        r = n/2
        
        
        if r > 0:
            d.append(r)
        
        order(d)
        
        if l > 0:
            d.append(l)
        
        order(d)
    
    return r, l


def order(d):
    # use bubblesort ish
    
    i = len(d)-1
    while i-1 >= 0 and d[i-1] < d[i]:
        # swap them
        d[i-1], d[i] = d[i], d[i-1]
        i -= 1