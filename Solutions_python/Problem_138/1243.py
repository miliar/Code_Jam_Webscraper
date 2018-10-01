fl=file("D-large.in","r")
fo=file("output4.txt","w")
t=int(fl.readline())
for i in xrange(t):
    n=int(fl.readline())
    player1=map(float,fl.readline().split())
    player2=map(float,fl.readline().split())
    cheat=0
    player1.sort()
    player2.sort()
    p1=n-1
    p2=n-1
    count=0
    while count<n:
        if(player1[p1]>player2[p2]):
            cheat+=1
            p1-=1
            p2-=1
        else:
            p2-=1
        count+=1
    good=0
    p1,p2=n-1,n-1
    count=0
    while count<n:
        if player1[p1]>player2[p2]:
            good+=1
            p1-=1
        else:
            p1-=1
            p2-=1
        count+=1
    fo.write("Case #%d: %d %d\n"%(i+1,cheat,good))
fl.close()
fo.close()
