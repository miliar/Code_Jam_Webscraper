import math, sys

f = [1 for i in range(707106)]

for i in range(2, 707106):
    if i % 10000000 == 0: print(i)
    f[i] = i**2 - f[i-1]
f[0] = 0

fin = open("input.in", 'r')
T = int(fin.readline())
sys.stdout = open("output2.out", 'w')

for tt in range(1, T + 1):
    r, t = [int(x) for x in fin.readline()[:-1].split()]
    low = 0
    hei = 70000
    mid = 0
    while low < hei:
        mid = (low + hei) // 2
        x = int(mid*2-1 + r)
        if (f[x] - f[r-1]) > t:
            hei = mid - 1
        elif f[x] - f[r-1] < t:
            low = mid + 1
        else:
            break
    
    if f[r+1] - f[r] > t:
        ans = 0
    else:
        x = int((mid)*2-1 + r)
        if f[x] - f[r-1] > t:
            #print("--1")
            ans = mid - 1
            
            x = int((mid-1)*2-1 + r)
            if f[x] - f[r-1] > t:
                ans = mid-2
        else:
            ans = mid
            x = int((mid+1)*2-1 + r)
            #print("--2")
            if f[x] - f[r-1] <= t:
                ans = mid + 1
                #print("--3")
        
        
    print("Case #" + str(tt) + ": " + str(ans))


fin.close()
sys.stdout.close();
