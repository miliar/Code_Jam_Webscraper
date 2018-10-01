cases = []
with open('A-large.in') as f:
    n = int(f.readline())
    for i,line in enumerate(f):
        s,total = 0,0
        smax,digits = line.split()
        for j,k in enumerate(digits):
            if total < j:
                s += j-total
                total += j-total
            total += int(k)
        cases.append('Case #'+str(i+1)+': '+str(s)+'\n')

with open('A-large-attempt0.out','w+') as g:
    g.writelines(cases)