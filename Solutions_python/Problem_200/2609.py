def fun(n):
    n=list(n)
    for i in range(len(n)-1,0,-1):
            if int(n[i-1])>int(n[i]):
                n[i-1]=str(int(n[i-1])-1)
                for j in range(i,len(n),1):
                    n[j]="9"
    s=""
    for i in range(0,len(n),1):
            s=s+n[i]
    return str(int(s))
a=input()
for l in range(a):
	se=raw_input()
	e=fun(se)
	print "Case #"+str(l+1)+": "+e
	