f=open("B-large.in","r")
out=open("1.txt","w")
T=int(f.readline())
for i in range(T):
    s=f.readline().replace("\n","").split(" ")
    C=float(s[0])
    F=float(s[1])
    X=float(s[2])
    if C>=X:
        print "Case #"+str(i+1)+": "+str(X/2)
        out.write("Case #"+str(i+1)+": "+str(X/2)+"\n")
        continue
    t=C/2;
    #count=C
    v=2
    while (X-C)/v>X/(v+F):
        v+=F
        t+=C/v
  
    t+=(X-C)/v
     
    print "Case #"+str(i+1)+": "+str(t)
    out.write("Case #"+str(i+1)+": "+str(t)+"\n")
    
f.close()
out.close()
     
    