def getPermutations(words):
    wc=len(words)
    pos=[[i,-1] for i in range(wc)]
    rs=[]
    next=True
    while next:
        rs.append(''.join(words[p[0]] for p in pos))
        next=False
        for i in range(wc-1,0,-1):
            if pos[i]==[0,-1] or pos[i]==[wc-1,1]:
                continue
            p = pos[i][0]+pos[i][1]
            for j in range(wc):
                if pos[j][0]==p:break
            if j>i:continue
            pos[i][0],pos[j][0]=pos[j][0],pos[i][0]
            for j in range(i+1,wc):
                pos[j][1]=-pos[j][1]
            next=True
            break
    return rs

if __name__ == '__main__':
    f = open('e:\\B-small-attempt0.in')
    fout = open('e:\\result.out', 'w')

    ccase = int(f.readline().strip())
    print ccase
    for icase in range(ccase):
        bases = [int(base) for base in f.readline().split()]
        print bases
        num=bases[0]
        allnum = [int(n) for n in getPermutations(str(num)+'0')]
        #print allnum
        m=-1
        for i in allnum:
            if i>num and (m==-1 or i<m):
                m=i
        fout.write('Case #%d: %d\n'%(icase+1, m))
        print 'Case #%d: %d'%(icase+1, m)
    f.close()
    fout.close()
