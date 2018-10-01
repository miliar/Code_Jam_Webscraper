import sys
results=[]


fin = open("A-small-attempt0.in", "r")
T=int(fin.readline())
for t in range(T):
    r,volume_total = fin.readline().split()
    r=int(r)
    volume_total = int(volume_total)
    i=0
    while(volume_total>=0):
        i+=1
        volume_needed=((r+1)**2)-(r**2)
        volume_total-=volume_needed
        r+=2
    results.append(i-1)

for t in range(T):
    print("Case #",end="")
    print(t+1,end="")
    print(": ",end="")
    print(results[t])

