def allocate(n, k, i):
    left = (n-1)/2 if (n%2==1) else n/2-1
    right = (n-1)/2 if (n%2==1) else n/2
    if (k==1): 
        print "Case #{}: {} {}".format(i, right, left)
    elif (k%2==0):
        return allocate(right, k/2, i)
    else:
        return allocate(left,(k-1)/2, i)
        
t = int(raw_input())

for i in xrange(1, t + 1):
    n,k = [int(c) for c in raw_input().split(" ")]
    allocate(n,k,i)
    
