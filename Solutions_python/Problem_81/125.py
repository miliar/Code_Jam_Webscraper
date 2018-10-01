
f = open('A-large.in','r')
T = int(f.readline().strip())

for ti in xrange(1,T+1):
    n = int(f.readline())
    arr,wp,owp,oowp = [],[],[],[]
    d = {}
    for i in xrange(n):
        x = f.readline().strip()
        arr.append(x)
        total,won = 0.0,0
        for xi in x:
            if xi=='1' or xi=='0':
                total +=1
                if xi=='1': won+=1
        wp.append(won/total)
        for j in xrange(n):
            if x[j]=='1': 
                d[(i,j)] = (won-1.0)/(total-1.0)
            elif x[j]=='0':
                d[(i,j)] = (won)/(total-1.0)
                
    for i in xrange(n):
        total,owpi = 0.0,0.0
        for j,x in enumerate(list(arr[i])):
            if x=='1' or x=='0':
                if j==i: continue
                owpi += d[(j,i)]
                total += 1
        owp.append(owpi/total)

    for i in xrange(n):
        total,oowpi = 0.0,0.0
        for j,x in enumerate(list(arr[i])):
            if x=='1' or x=='0':
                oowpi += owp[j]
                total += 1
        oowp.append(oowpi/total)

    print 'Case #%d:'%(ti)
    for i in xrange(n):
        print 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]
