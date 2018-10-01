def solve():
    D,N= [int(e) for e in input().split()]
    speed=10**100

    for j in range(N):
        k,s=[int(e) for e in input().split()]
        t = (s*D)/(D-k)
        if t < speed:
            speed=t

    return str(speed)
    
T=int(input());
 
for t in range(1,T+1):
    print ("Case #" + str(t) + ": " + solve())
