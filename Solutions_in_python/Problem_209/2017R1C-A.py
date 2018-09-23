file = open("c:/CodeJam/2017/R1/A-large.in")
line = file.readline()

from math import pi
## Number of Test Cases:  1<=T<=100
T=int(line)

## Tests each case
for testcase in range(T):
    [n,k] = file.readline().split()
    # N = Number of Pancakes Available
    N=int(n)
    #print('N= '+n)
    # K = Number of Pancakes Ordered
    K=int(k)
    
    listofavailablepancakes=[]
    listofsideareas=[]
    pancakearea=0
    bigpancake=0
    bigindex=0
    maxsurfacearea=0

    for i in range(N):
        [r,h] = map(int,file.readline().split())
        listofavailablepancakes.append([i,r,h,2*pi*r*h,pi*r*r])

    listofavailablepancakes.sort(key=lambda x: -x[1])

    sortedradius=list(listofavailablepancakes)

    listofavailablepancakes.sort(key=lambda x: -x[3])

    sortedsidewall=list(listofavailablepancakes)
    
    for i in range(N-K+1):
        bigpancake=sortedradius[0]

        sortedradius.remove(bigpancake)
        sortedsidewall.remove(bigpancake)

        totalsurfacearea=bigpancake[3]+bigpancake[4]
        for j in range(K-1):
            totalsurfacearea+=sortedsidewall[j][3]

        if totalsurfacearea>maxsurfacearea:
            maxsurfacearea=totalsurfacearea
        
        

    print('Case #{}: {}'.format(testcase+1,maxsurfacearea))
           
file.close() 
        
        
    

    
    

