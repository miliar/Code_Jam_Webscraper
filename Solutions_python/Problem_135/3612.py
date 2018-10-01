f = open('A-small-attempt0.in', 'ro')
g = open('A-small-attempt0.out', 'w')

input = f.readlines()
casecnt = input[0]

for i in xrange(int(casecnt)):
    
    nthrow1 = input[(i*10)+1]
    nthrow2 = input[(i*10)+6]
    
    row1 = input[(i*10)+1+int(nthrow1)]
    row2 = input[(i*10)+6+int(nthrow2)]
    
    set1 = set(row1.split())
    set2 = set(row2.split())
    
    inter = set1 & set2
    
    if len(inter) > 1:
        g.write('Case #' + str(i+1) + ': Bad magician!\n')
    elif len(inter) == 0:
        g.write('Case #' + str(i+1) + ': Volunteer cheated!\n')
    else:
        g.write('Case #' + str(i+1) + ': ' + list(inter)[0] + '\n')