def canwinall(nblocks, kblocks):
    for i in range(len(nblocks)):
        if nblocks[i] < kblocks[i]:
            return False
    return True

infile = open('D-small-attempt0.in','r')
outfile = open('war.out.txt','w')

cases = int(infile.readline().strip())
for case in range(1,cases+1):
    numblocks = int(infile.readline().strip())
    nblocks = infile.readline().strip().split()
    kblocks = infile.readline().strip().split()
    mynblocks = []
    mykblocks = []
    for n in nblocks:
        n = float(n)
        mynblocks.append(n)
    for k in kblocks:
        k = float(k)
        mykblocks.append(k)

    nblocks.sort()
    kblocks.sort()
    mynblocks.sort()
    mykblocks.sort()
    
    warnpoints = 0
    for i in range(numblocks):
        nchosen = nblocks.pop(0)
        ksmall = 1.01
        for k in kblocks:
            if nchosen < k:
                ksmall = k
                break
        if ksmall == 1.01:
            kblocks.pop(0)
            warnpoints += 1
        else:
            kchosen = kblocks.pop(kblocks.index(ksmall))

    dwarnpoints = 0
    nblocks = mynblocks
    kblocks = mykblocks
    for i in range(numblocks):
        if canwinall(nblocks, kblocks):
            dwarnpoints += len(nblocks)
            break
        else:
            nblocks.pop(0)
            kblocks.pop()
    outfile.write('Case #'+str(case)+': '+str(dwarnpoints)+' '+str(warnpoints)+'\n')

outfile.close()
