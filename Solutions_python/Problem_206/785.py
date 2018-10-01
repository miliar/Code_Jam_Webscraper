x = input()

for i in range(x):
    d,n = raw_input().split()
    d = int(d)
    n = int(n)
    maxh = 0
    for j in range(n):
        k,s = raw_input().split()
        k = int(k)
        s = int(s)
        if ((d-k)/(s*1.0))>maxh:
            maxh = (d-k)/(s*1.0)
    print ("Case #" + str(i+1) + ": " + '{0:.6f}'.format(d/(maxh*1.0)))
    
