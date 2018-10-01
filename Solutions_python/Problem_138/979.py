import math

inputs = open("in.txt").readlines()
output = open('out.txt', 'w')
t = int(inputs[0])
for i in range(1, t + 1):
    r = (i - 1) * 3 + 1
    n = int(inputs[r])
    
    naomi = [float(x) for x in inputs[r + 1].rstrip().split(" ")]
    ken = [float(x) for x in inputs[r + 2].rstrip().split(" ")]
    
    naomi = sorted(naomi)
    ken = sorted(ken)
    
    #print(naomi)
    #print(ken)
    
    naomic=naomi[:]
    kenc=ken[:]
    
    dcount = 0
    while len(naomic) > 0:
        if naomic[len(naomic) - 1] < kenc[len(kenc) - 1]:
            #trick ken to giving up his best piece
            naomic.pop(0)
            kenc.pop()
        else:
            naomic.pop()
            kenc.pop()
            dcount+=1
        #print(naomic)
        #print(kenc)
                
    wcount = 0
    kp = 0
    while len(naomi) > 0:
        lowestNaomi = naomi.pop(0)
        for k in range(kp, n):
            if(ken[k] > lowestNaomi):
                #print(lowestNaomi, ken[k], k)
                kp = k + 1
                wcount += 1
                break
              
         
    answer = "Case #%d: %d %d\n"%(i,dcount,n - wcount)
    #print(answer)
    output.write(answer)
output.close()
