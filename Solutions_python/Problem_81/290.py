case = int(raw_input())
for tt in range(1,case+1):
    team = int(raw_input())
    stat = []
    liswp = []
    lisowp = []
    lisoowp = []
    ans = []
    for i in range(team):
        stat.append(raw_input())
    for i in range(len(stat)):
        liswp.append(float(stat[i].count('1'))/float(len(stat[i]) - stat[i].count('.')))
    for i in range(len(stat)):
        opp = len(stat[i]) - stat[i].count('.')
        owp = 0
        for j in range(len(stat[i])):
            if(stat[i][j] != '.'):
                wwp = stat[j].count('1')
                if(stat[j][i] == '1'):
                    wwp -= 1
                owp += float(wwp)/float(team - stat[j].count('.') -1)
        lisowp.append(float(owp)/float(opp))
    for i in range(len(stat)):
        oowp = 0
        opp = len(stat[i]) - stat[i].count('.')
        for j in range(len(stat[i])):
            if(stat[i][j] != '.'):
                oowp += lisowp[j]
        lisoowp.append(float(oowp)/float(opp))
    for i in range(len(liswp)):
        ans.append(0.25*liswp[i] + 0.5*lisowp[i] + 0.25*lisoowp[i])
    print 'Case #' + str(tt) + ':'
    for i in ans:
        print i
