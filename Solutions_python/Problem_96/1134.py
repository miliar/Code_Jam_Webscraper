import sys,operator
sur = {0:[(0,0,0),(-1,+1,0)],1:[(1,0,0)],2:[(1,1,0),(2,0,0)]}
with open(sys.argv[1]) as fp:
    T=int(fp.readline())
    for i in range(1,T+1):
        instr=map(int,fp.readline().split())
        N,S,p=instr[0:3]
        result=[]
        for num in instr[3:]:
            triplets = (num/3,)*3
            rem = num % 3
            result.append([x for x in (map(operator.add,triplets,x) for x in sur[rem]) if max(x) <= 10 and min(x) >= 0])
        for r in result:
            if not S: break
            if len(r) > 1 and max(r[-1])>=p and max(r[0]) < p:
                del r[0]
                S-=1
        print "Case #{0}: {1}".format(i,len([s for s in result if max(s[0]) >= p]))
        
                
                
            
