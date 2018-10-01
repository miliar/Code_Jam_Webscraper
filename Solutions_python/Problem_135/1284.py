import os
from collections import defaultdict
__author__ = 'steven'

question='qa'
fs={'t1','small','big'}

def solver(fa,fmat,sa,smat):
    #buid dict
    dt=dict()
    for j in range(0,4):
        for k in range(0,4):
            fr=j;
            for kk in range(0,4):
                if fmat[j][k] in smat[kk]:
                    sr=kk;
                    break;
            if not (fr,sr) in dt:
                dt[(fr,sr)]=list()
            dt[(fr,sr)].append(fmat[j][k])
    if not (fa-1,sa-1) in dt:
        return 'Volunteer cheated!'
    if len( dt[(fa-1,sa-1)])>1:
        return 'Bad magician!'
    return  '%d'%(dt[(fa-1,sa-1)][0])


for s in fs:
    print question+s
    f='./'+question+s
    if os.path.isfile('./'+question+s):
        ls=open(f)
        noq=(int)(ls.readline())
        fout=open(question+s+'-a','w')
        print noq
        for i in range(0,noq):
            fa=(int)(ls.readline())
            fmat=[[0 for x in xrange(4)] for x in xrange(4)]
            for j in range(0,4):
                lint=ls.readline().strip().split()
                for k in range(0,4):
                    fmat[j][k]=int(lint[k])
            print fmat
            sa=(int)(ls.readline())
            smat=[[0 for x in xrange(4)] for x in xrange(4)]
            for j in range(0,4):
                lint=ls.readline().strip().split()
                for k in range(0,4):
                    smat[j][k]=int(lint[k])
            print smat
            fout.write('Case #%d: %s\n'%(i+1,solver(fa,fmat,sa,smat)))

#Case #1: 7
#Case #2: Bad magician!
#Case #3: Volunteer cheated!


