clo = open("output.txt", 'w')

with open("input.txt") as f:
    t = int(f.readline())
    for test in range(1,t+1):
        ans=0
        m=0
        d,n=map(int,f.readline().strip().split())

        for h in range(n):
            k,s=map(int,f.readline().strip().split())
            m=max(m,(float)(d-k)/s)

        ans=d/m
        clo.write("Case #" + str(test) + ": " + str(ans))

        clo.write('\n')