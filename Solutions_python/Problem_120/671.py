t=input()
for y in range(t):
    r,t=[long(x) for x in raw_input().split(" ")]
    c=0
    while t>=0:
        t+=(r**2-(r+1)**2)
        c+=1
        if t<0:
            break
        r+=2
        #print r
    print "Case #"+str(y+1)+": "+str(c-1)
