inpf=open('input.txt')
T=int(inpf.readline()[:-1])
out=''

for case in range(1,T+1):
    data=inpf.readline().split()
    C=int(data.pop(0))
    coms=data[:C]
    del data[:C]
    D=int(data.pop(0))
    opps=data[:D]
    inv=data[-1]

    coms2={}
    for com in coms:
        coms2[com[:2]]=com[2]
        coms2[com[1]+com[0]]=com[2]
    coms=coms2

    bases='QWERASDF'
    opps2={}
    for base in bases:
        opps2[base]=[]
    for opp in opps:
        opps2[opp[0]].append(opp[1])
        opps2[opp[1]].append(opp[0])
    opps=opps2

    L=''

    for i,el in enumerate(inv):
        if not L:
            L=el
        elif el+L[-1] in coms:
            L=L[:-1]+coms[el+L[-1]]
        else:
            for opp in opps[el]:
                if opp in L:
                    L=''
                    break
            else:
                L+=el

    out+='Case #{}: {}\n'.format(case,'['+', '.join(list(L))+']')

outf=open('output.txt',mode='w')
print(out[:-1],end='',file=outf)
outf.close()
inpf.close()
