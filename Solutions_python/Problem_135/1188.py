__author__ = 'fabrizio'

with open("input.txt") as f:
    T=int(f.readline().strip())
    for t in range(T):
        q1=int(f.readline().strip())-1
        grid1=[]
        for row in range(4):
            grid1.append(map(int,f.readline().strip().split()))
        q2=int(f.readline().strip())-1
        grid2=[]
        for row in range(4):
            grid2.append(map(int,f.readline().strip().split()))
        res=0
        ans=0
        for i in range(4):
            for j in range(4):
                if grid1[q1][i]==grid2[q2][j]:
                    res=res+1
                    ans=grid1[q1][i]
        print "Case #"+str(t+1)+": "+("Volunteer cheated!" if res==0 else (str(ans) if res==1 else "Bad magician!"))
