import Queue as Q

def solve(stalls, ppl):
    if stalls == ppl:
        return "0 0"
    if float(ppl)/stalls > 0.6:
        return "0 0"
    space = Q.PriorityQueue()
    space.put(-stalls)
    
    while ppl > 1:
        ppl = ppl - 1
        max_s = -space.get()
        left = 0
        if max_s % 2 == 0:
            left = max_s/2 - 1
        else:
            left = max_s/2
        right = max_s - 1 - left
        space.put(-right)
        space.put(-left)
        #print list(space.queue)

    max_s = -space.get()
    
    max_s -= 1
    left = 0
    right = 0
    
    left = max_s/2
    
    right = max_s - left
    #print str(left) + " " + str(right)
    smallest = min(left, right)
    largest = max(left, right)

    res = "" + str(largest) + " " + str(smallest)
    return res
    
t=int(raw_input())
for cas in xrange(1,t+1):
    n=str(raw_input())
    arra = n.split()
    stalls = int(arra[0])
    ppl = int(arra[1])
    print "Case #{}: {}".format(cas,solve(stalls, ppl))
