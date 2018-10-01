import sys
t=int(raw_input())
for case in range(t):
    p=int(raw_input())
    naomi=map(float,raw_input().split())
    ken=map(float,raw_input().split())
    naomi.sort()
    ken.sort()
    naomi_c=naomi[::-1]
    ken_c=ken[::-1]
    nc=0
    n=0
    for i in range(p):
##        print naomi,ken
        #cheating
        if naomi[0]<ken[0]:
            ken.remove(ken[-1])
            naomi.remove(naomi[0])
        else:
##            print "safd"
            ken.remove(ken[0])
            naomi.remove(naomi[0])
            nc+=1
    naomi=naomi_c[::]
    ken=ken_c[::]
    for i in range(p):
##        print naomi,ken
        if naomi[0]>ken[0]:
            naomi.remove(naomi[0])
            ken.remove(ken[-1])
            n+=1
        else:
            naomi.remove(naomi[0])
            ken.remove(ken[0])
            
    print "Case #"+str(case+1)+": "+str(nc)+" "+str(n)
    
