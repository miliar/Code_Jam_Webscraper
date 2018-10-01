def solve(end,dist,speed):
    times = []
    for i in range(len(dist)):
        d = end - dist[i]
        times.append(d/speed[i])
    lowest = -1
    for i in times:
        if(i > lowest):
            lowest = i
    solut = end/lowest
    return solut
t = int(input())
for i in range(1,t+1):
    dist = []
    speed = []
    d,n = input().split(" ")
    for f in range(int(n)):
        k,s = input().split(" ")
        dist.append(int(k))
        speed.append(int(s))
    print("Case #{}: {:0.6f}".format(i,solve(int(d),dist,speed)))
