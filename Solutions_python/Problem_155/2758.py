def solve(a):
    standing=0
    not_standing=[]
    require=0
    for i in range(len(a)):
      l=0  
      if(a[i]!=0):  
        if(standing>=i):
            standing+=a[i]
        else:
            l+=i-standing
            standing+=(a[i]+l)
            require+=l
    return require
T=input()
for i in range(T):
    in1=raw_input().strip().split()
    lis=[int(x) for x in list(in1[1])]
    print "Case #"+str(i+1)+": "+str(solve(lis))
