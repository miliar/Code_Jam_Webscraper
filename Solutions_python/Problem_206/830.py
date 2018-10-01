
def solve(D,N,horses):
    maxspeed = float('Inf')

    for i in range(N-1,-1,-1):
        [pos,speed] = horses[i]
        
        """
        time = (D-pos) / speed

        mustspeed = D / time

        maxspeed = min(maxspeed,mustspeed)
        """

        if maxspeed * (D-pos) > D * speed:
            maxspeed = D * speed / (D-pos)

    return maxspeed

f=open("A-large.in","r")
g=open("output.txt","w")

T=int(f.readline())

for i in range(T):
    [D,N] = [int(j) for j in f.readline().split()]

    horses = [[int(j) for j in f.readline().split()] for k in range(N)]

    ans = solve(D,N,horses)

    g.write("Case #{}: {}\n".format(i+1,ans))

f.close()
g.close()
