tbl  = {('1','1'):'1',('1','i'):'i',('1','j'):'j',('1','k'):'k',
        ('i','1'):'i',('i','i'):'-1',('i','j'):'k',('i','k'):'-j',
        ('j','1'):'j',('j','i'):'-k',('j','j'):'-1',('j','k'):'i',
        ('k','1'):'k',('k','i'):'j',('k','j'):'-i',('k','k'):'-1'}

def mult(a,b):
    p = tbl[(a[-1],b[-1])]
    if len(a) == len(b):
        return p
    if p[0] == '-':
        return p[1]
    return '-'+p

cases = []
with open('C-small-attempt2.in') as f:
    n = int(f.readline())
    el,ex = 0,0
    for i,line in enumerate(f):
        if i%2 == 0:
            el,ex = [int(x) for x in line.split()]
        elif el == 1:
            cases.append('Case #'+str(i//2+1)+': NO\n')
        else:
            string = ''
            state = 'S'
            total = '1'
            prod = '1'
            for x in range(ex):
                for c in line:
                    if c != '\n':
                        prod = mult(prod,c)
                        if state == 'S' and prod == 'i':
                            state = 'I'
                            prod = '1'
                        if state == 'I' and prod == 'j':
                            state = 'J'
                            prod = '1'
                        if state == 'J' and prod == 'k':
                            state = 'K'
                            prod = '1'
            if state == 'K' and prod == '1':
                cases.append('Case #'+str(i//2+1)+': YES\n')
            else:
                cases.append('Case #'+str(i//2+1)+': NO\n')

with open('C-small-attempt2.out','w+') as g:
    g.writelines(cases)