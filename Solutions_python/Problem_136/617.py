def calc():
    numList=list(map(float,fin.readline().split(' ')))
    c=numList[0]
    f=numList[1]
    x=numList[2]
    rate=2.0
    timeUsed=0.0
    timeLeft=x/rate
    time=timeUsed+timeLeft
    best=time
    mustGo=True
    while mustGo:
        timeUsed+=c/rate
        rate+=f
        timeLeft=x/rate
        time=timeUsed+timeLeft
        if time<best:
            best=time
        else:
            mustGo=False
    return best

if __name__=='__main__':
    fin=open('input.txt','r')
    fout=open('output.txt','w')
    cases=int(fin.readline())
    for i in range(1,cases+1):
        fout.write('Case #{}: {:.7f}\n'.format(i,calc()))
    fin.close()
    fout.close()
