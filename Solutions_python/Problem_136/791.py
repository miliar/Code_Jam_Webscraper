#Read input file with extension .in
#for path in files:
#    if path.find('.in') != -1:
#        break
#print path
path ='B-large.in'
f = open(path)
o = open('output.out','w')
cases=int(f.readline())


for case in xrange(1,cases+1):
    [C,F,X] = [float(z) for z in f.readline().strip().split(' ')]
    farms = 0
    n=-1
    mi=float('inf')
    while farms<mi:
        n+=1
        if n:
            farms += C/(2+(n-1)*F)
        T=farms+X/(2+n*F)
        if T < mi:
            mi=T
    o.write('Case #%d: %.7f\n' %(case,mi))
    
    


f.close()
o.close()
