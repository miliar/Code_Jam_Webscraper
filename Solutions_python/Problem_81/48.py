for c in xrange(int(raw_input())):
    n=int(raw_input())
    sched=[]
    wins=[]
    losses=[]
    for i in xrange(n):
        tmp=raw_input()
        wins.append(0.0)
        losses.append(0.0)
        for g in tmp:
            if g=='1':
                wins[i]+=1
            elif g=='0':
                losses[i]+=1
        sched.append(tmp)
    owp=[]
    for i in xrange(n):
        total=0.0
        for g in xrange(n):
            if sched[i][g]=='1':
                total+=wins[g]/(wins[g]+losses[g]-1)
            elif sched[i][g]=='0':
                total+=(wins[g]-1)/(wins[g]-1+losses[g])
        owp.append(total/(wins[i]+losses[i]))
    oowp=[]
    for i in xrange(n):
        total=0.0
        for g in xrange(n):
            if sched[i][g]=='1' or sched[i][g]=='0':
                total+=owp[g]
        oowp.append(total/(wins[i]+losses[i]))
    print "Case #%d:" % (c+1)
    for i in xrange(n):
        print (0.25*wins[i]/(wins[i]+losses[i])+0.5*owp[i]+0.25*oowp[i])
