T=int(raw_input())
for i in range(T):
    Smax,A=raw_input().split()
    Smax=int(Smax)
    c=1
    count=0
    staus= []
    stand_people = int(A[0])
    for i in range(1,Smax+1):
    	if (stand_people>=Smax):
    		break
        if ((stand_people>=i) or (int(A[i])==0) ):
            stand_people+=int(A[i])
        else:
            count+=(i - stand_people)
            stand_people+=int(A[i])+(i - stand_people)
    print "Case #%d: %d" %(T, count)        