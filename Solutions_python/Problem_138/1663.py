def PlayWar(nblocks,kblocks):
    nblocks.sort()
    
    kblocks.sort()
    
    score = 0
    while (len(nblocks) > 0):
        naomi = nblocks[-1]
        nblocks.remove(naomi)
        for k in kblocks:
            
            if k > naomi:
                kblocks.remove(k)
                
                break
            if k < naomi and k == kblocks[-1]:
                kblocks.remove(kblocks[0])
                
                score = score+1

    return score

def CheatWar(nblocks,kblocks):
    nblocks.sort()
    kblocks.sort()
    
    x = 7
    y = 6
    while x > y:
        x = len(nblocks)
        for i in range(len(nblocks)):
            if kblocks[i] > nblocks[i]:
                nblocks.remove(nblocks[0])
                kblocks.remove(kblocks[-1])
                break
        y = len(nblocks)

    score = len(nblocks)
    return score

f1=open('C:/Python27/thing', 'w+')

linelist = []
for line in open('C:\Users\User\Downloads\D-large.in'):
    linelist.append(line.rstrip('\n'));

testnum = int(linelist[0]);

for i in xrange(testnum):
    naomi1 = linelist[3*i+2]
    ken1 = linelist[3*i+3]
    n1=naomi1.split()
    k1=ken1.split()
    deception = CheatWar(n1,k1)
    n2=naomi1.split()
    k2=ken1.split()
    honest = PlayWar(n2,k2)

    f1.write("Case #"+str(1+i)+": "+str(deception)+" "+str(honest)+"\n")

    
f1.close()

