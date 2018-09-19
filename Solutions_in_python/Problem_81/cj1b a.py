def wp(arr, x):
    games=len(arr)
    if x!=-1:
        games-=1
    wins=0
    for a in range(len(arr)):
        if a!=x:
            if arr[a]==-1:
                games-=1
            if arr[a]==1:
                wins+=1
    return float(wins)/float(games)

inf=open('cj1ba_inputl.txt','r')
of=open('cj1ba_output.txt','w')
cases=int(inf.readline())

for c in range(cases):
    teams=int(inf.readline())
    inp=''
    for a in range(teams):
        inp+=inf.readline().strip('\n')
    arr=[]
    for a in range(teams):
        arr+=[[]]
        for b in range(teams):
            if inp[a*teams+b]=='.':
                arr[a]+=[-1]
            else:
                arr[a]+=[int(inp[a*teams+b])]

    wps=[]
    for a in range(teams):
        wps+=[[wp(arr[a],-1)]]
        for b in range(teams):
            wps[a]+=[wp(arr[a],b)]

    owps=[]
    for a in range(teams):
        opps=0
        sumwp=0
        owps+=[0]
        for b in range(teams):
            if arr[a][b]!=-1:
                opps+=1
                sumwp+=wps[b][a+1]
        owps[a]=sumwp/float(opps)

    oowps=[]
    for a in range(teams):
        oowps+=[0]
        opps=0
        sumowp=0
        for b in range(teams):
            if arr[a][b]!=-1:
                opps+=1
                sumowp+=owps[b]
        oowps[a]=sumowp/float(opps)
                
    rpis=[]
    for a in range(teams):
        rpis+=[0.25*wps[a][0]+0.5*owps[a]+0.25*oowps[a]]

    of.write('Case #'+str(c+1)+':\n')
    for a in range(teams):
        of.write(str(rpis[a])+'\n')

inf.close()
of.close()
