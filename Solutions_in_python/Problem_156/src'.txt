fil=open("C:\Users\Sharad Boni\Downloads\B-small-attempt6.in")
t=int(fil.readline().strip("\n"))
f=open("C:\Users\Sharad Boni\Desktop\srcoutput.txt","w")

for bd in xrange(t):
    s=[]
    l=[]
    
    no=int(fil.readline().strip("\n"))
    if no>1:
        l=map(int,fil.readline().strip("\n").split(" "))
    else:
        l.append(int(fil.readline().strip("\n")))
    maxy=max(l)  
    ans=maxy
    for i in xrange(1,maxy+1):
        now=0
        maxx=0
        for j in xrange(1,no+1):
            if l[j-1]>i:
                if l[j-1]%i==0:
                    z=0
                else:
                    z=1    
                now+=(l[j-1]/i)+(z)-1
                maxx=max(maxx,i)
            else:
                maxx=max(maxx,l[j-1])    
        now+=maxx
        if now<ans:
            ans=now
                                           
    print "Case #"+str(bd+1)+": "+str(ans)
    f.write("Case #"+str(bd+1)+": "+str(ans)+"\n")
         
    