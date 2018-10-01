T=int(input())
for case in range(1,T+1):
    R1=list()
    R2=list()
    ANS=list()
    t=int(input())
    for r in range(1,5):
        k=input()
        if r==t:
            R1=k.split(' ')
    #print(t,R1)
    t=int(input())
    for r in range(1,5):
        k=input()
        if r==t:
            R2=k.split(' ')
    #print(t,R2)
    ANS=[x for x in R1 if (x in R2)]
    
    if len(ANS)==0:
        print('Case #',case,': Volunteer cheated!',sep='')
    elif len(ANS)==1:
        print('Case #',case,': ',ANS[0],sep='')
    else:
        print('Case #',case,': Bad magician!',sep='')
