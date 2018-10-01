t=int(raw_input())
case=1
while case<=t:
    r1=int(raw_input())
    r1=r1-1
    i=0
    while i<4:
        if(r1==i):
            a=[int(r) for r in raw_input().split()]
        else:
            raw_input()
        i+=1

    r2=int(raw_input())
    r2=r2-1
    i=0
    while i<4:
        if(r2==i):
            b=[int(r) for r in raw_input().split()]
        else:
            raw_input()
        i+=1

    match,i,j=0,0,0
    x=0
    while i<4:
        j=0
        while j<4:
            if(a[i]==b[j]):
                match+=1
                x=i
            j+=1
        i+=1
    if(match==1):
        print "Case #" + str(case) + ": " + str(a[x])
    elif match>1:
        print "Case #" + str(case) + ": " + "Bad magician!"
    else:
    	print "Case #" + str(case) + ": " + "Volunteer cheated!"
    case+=1
    
            

    
