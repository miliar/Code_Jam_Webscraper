import sys




def solve(K, horses):

   horses = sorted(horses, key=lambda i:i[0])

   amax = 0
   for h in reversed(horses):
       a = (K - h[0])/h[1]
       if a>amax: amax=a

   return K/amax
   
 


T = int(input())
for t in range(T):
    horses = []
    nkil, nhorses = [int(i) for i in input().split()]
    for n in range(nhorses):
        kil, v = [float(i) for i in input().split()]
        horses.append((kil,v))

    s = solve(nkil, horses)
    print ("Case #%i: %.6f"%(t+1,s) )

    
