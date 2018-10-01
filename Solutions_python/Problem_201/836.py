t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    rmax, rmin=0, 0
    while(k!=0):
        if (n%2==1):
            rmax, rmin=n//2, n//2
            n, k= n//2, k//2
        else:    
            rmax, rmin=n//2, (n//2)-1
            if (k%2==1):
                n, k= (n//2)-1, k//2
            else:
                n, k= n//2, k//2                
    print("Case #{}: {} {}".format(i, rmax, rmin))