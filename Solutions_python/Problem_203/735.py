import random
import copy

def extend(carte,lx,cx,nLine,nCol):
    top=lx
    bot=lx
    left=cx
    right=cx
    modif=True
    while modif:
        print top,bot,left,right
        modif=False
        if top>0:
            good=True
            for c in range(left,right+1):
                if carte[top-1][c]!='?':
                    good=False
                    break
            if good:
                modif=True
                for c in range(left,right+1):
                    carte[top-1][c]=carte[lx][cx]
                top-=1
        if left>0:
            good=True
            for l in range(top,bot+1):
                if carte[l][left-1]!='?':
                    good=False
                    break
            if good:
                modif=True
                for l in range(top,bot+1):
                    carte[l][left-1]=carte[lx][cx]
                print carte[lx][cx]
                left-=1
        if bot<nLine-1:
            good=True
            for c in range(left,right+1):
                if carte[bot+1][c]!='?':
                    good=False
                    break
            if good:
                modif=True
                for c in range(left,right+1):
                    carte[bot+1][c]=carte[lx][cx]
                bot+=1
        if right<nCol-1:
            good=True
            for l in range(top,bot+1):
                if carte[l][right+1]!='?':
                    good=False
                    break
            if good:
                modif=True
                for l in range(top,bot+1):
                    carte[l][right+1]=carte[lx][cx]
                right+=1
    return carte


def solve(carte,nLine,nCol):
    visited=set(['?'])
    for l in range(nLine):
        for c in range(nCol):
            if carte[l][c] not in visited:
                carte=copy.deepcopy(extend(carte,l,c,nLine,nCol))
                visited.add(carte[l][c])
                for nl in carte:
                    print ''.join(nl)
                print visited
    return carte


fi=open('ex1.in')
fo=open('ex1.out','w')
nCases=int(fi.readline())

for case in range(1,nCases+1):
    carte=[]
    nLine,nCol=[int(tok) for tok in fi.readline().strip().split()]
    for l in range(nLine):
        carte.append(list(fi.readline().strip()))
    newcarte=solve(carte,nLine,nCol)
    for l in range(nLine):
        for c in range(nCol):
            #assert newcarte[l][c]!='?'
            if carte[l][c]!='?':
                assert newcarte[l][c]==carte[l][c]
    fo.write('Case #%s:\n' % case)
    for l in newcarte:
        fo.write(''.join(l)+'\n')

fi.close()
fo.close()
