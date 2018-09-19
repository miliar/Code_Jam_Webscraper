fin = file("B-small-attempt1.in", "rU")
fout = file("B-small-attempt1.out", "w")

nruns = int(fin.readline().strip())
for crun in xrange(nruns):
    line = fin.readline().strip().split()
    nboost = int(line[0])
    tbuild = int(line[1])
    nstars = int(line[2]) #not including star 0
    ndists = int(line[3])
    distseq = line[4:]

    #build cumulative distances
    cumdist = [0]
    for i in xrange(nstars):
        cumdist.append(cumdist[i]+int(distseq[i%ndists]))
    #print cumdist

    #0 boosters
    if nboost == 0:
        #result = 0
        #for i in xrange(nstars):
        #    result += int(distseq[i%ndists])*2
        result = cumdist[nstars]*2
            
    #1 booster
    elif nboost == 1:
        bestsaving = 0
        for i in xrange(nstars): #build here
            #time savings from i to i+1
            timeeffect = cumdist[i+1]*2 - tbuild
            timesaved = 0
            if timeeffect > 0: #savings possible
                timesaved = min(timeeffect, (cumdist[i+1]-cumdist[i])*2)
                timesaved /= 2
            bestsaving = max(bestsaving, timesaved)
        result = cumdist[nstars]*2-bestsaving
    
    #brute force up to 2 boosters
    elif nboost == 2:
        bestsaving = 0
        for i in xrange(nstars): #build here
            for j in xrange(i+1, nstars): #build second one here
                #time savings from i to i+1
                timeeffect = cumdist[i+1]*2 - tbuild
                timesaved = 0
                if timeeffect > 0: #savings possible
                    timesaved = min(timeeffect, (cumdist[i+1]-cumdist[i])*2)
                    timesaved /= 2
                #carry forward saving
                timeeffect2 = cumdist[j+1]*2 - timesaved - tbuild
                timesaved2 = 0
                if timeeffect2 > 0: #more savings possible
                    timesaved2 = min(timeeffect2, (cumdist[j+1]-cumdist[j])*2)
                    timesaved2 /= 2
                timesaved = timesaved + timesaved2
                bestsaving = max(bestsaving, timesaved)
        result = cumdist[nstars]*2-bestsaving
    

    strout = "Case #" + str(crun+1) + ": " + str(result) + "\n"
    #print strout
    fout.write(strout)
fin.close()
fout.close()
