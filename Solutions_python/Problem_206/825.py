t = int(input())  
for i in range(1, t + 1):
    d, n = [int(val) for val in input().split()] 

    tmax = 0
    for j in range(n):
        k, s = [int(val) for val in input().split()] 
        tt = (d - k) / s    
        if tt > tmax:
            tmax = tt
    
    res = d / tmax
    print("Case #{}: {:10.6f}".format(i, res))
