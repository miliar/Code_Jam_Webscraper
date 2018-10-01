import sys

ifile = open('a-small.in','r')
ofile = open('a-small.out','w')
sys.stdin = ifile
c = int(input())
for i in range(c):
    num = int(input())
    score=[]
    wp = {}
    owp=[]
    for j in range(num):
        cwp = input()
        score.append(cwp)
        ones = sum([1 for k in cwp if k=='1'])
        zeroes = sum([1 for k in cwp if k=='0'])
        wp[j]=[ones/(ones+zeroes),0,0]
        r=[]
        s=0
        t=0
        if ones+zeroes != 1:
            s=(ones-1)/(ones+zeroes-1)
            t=(ones)/(ones+zeroes-1) 
        for k in cwp:
            if k=='.':
                r.append(0)
            elif k=='1':
                r.append(s)
            else:
                r.append(t)
        owp.append(r)
    print("Case #%s:" %(i+1,),file=ofile)
    for j in range(num):
        k = score[j]
        s = 0
        index=0
        n=0
        for l in k:
            if l!='.':
                s+=owp[index][j]
                n+=1
            index+=1
        wp[j][1]=s/n
    for j in range(num):
        k=score[j]
        s=0
        index=0
        n=0
        for l in k:
            if l!='.':
                s+= wp[index][1]
                n+=1
            index+=1
        wp[j][2]=s/n
    for j in range(num):
        print("%.7f" %((0.25*(wp[j][0]+wp[j][2])+0.5*wp[j][1]),),file=ofile)

    
                
ifile.close()
ofile.close()
