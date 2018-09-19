def getOptimalWarResult(nb, kb):
    ncount = 0
    if len(nb) == 1 and nb[0] > kb[0]:
        return 1
    if len(nb) == 1 and nb[0] < kb[0]:
        return 0
    for neach in nb:
        max_list = [keach for keach in kb if keach > neach]
        if len(max_list) > 0:
            kpick = min(max_list)
        else:
            kpick = min([keach for keach in kb if keach < neach])
        kb.remove(kpick)
        if kpick < neach:
            ncount += 1
    return ncount

def checkDeceitValue(tn, kb):
    for each in kb:
        if tn == each:
            return False
    return True
    
def getDeceitfulWarResult(nblcks, kblcks):
    ncount = 0
    if len(nblcks) == 1 and nblcks[0] > kblcks[0]:
        return 1
    if len(nblcks) == 1 and nblcks[0] < kblcks[0]:
        return 0
    nblcks.sort()
    kblcks.sort()                  
    while len(nblcks) > 0:
        if nblcks[0] > kblcks[0]:
            ncount += 1
            nblcks.pop(0)
            kblcks.pop(0)
        else:
            told_nao = kblcks[-1] - 0.00001
            if checkDeceitValue(told_nao, kblcks):
                nblcks.pop(0)
                kblcks.pop(-1)
            
    return ncount
        
def warResult(nblcks, kblcks):
    nblk = nblcks[:]
    kblk = kblcks[:]
    res1 = getOptimalWarResult(nblcks, kblcks)
    res2 = getDeceitfulWarResult(nblk, kblk)
    return (res1, res2)

with open('D-large.in', 'r') as fp:
    for tc in xrange(int(fp.readline())):
        no_of_blocks = int(fp.readline())
        naomi_blcks = [float(i) for i in fp.readline().strip().split()]
        ken_blcks = [float(i) for i in fp.readline().strip().split()]
        res = warResult(naomi_blcks, ken_blcks)
        print "Case #%d: %d %d" % (tc+1, res[1], res[0])
