# fly outer racketThickness stringThickness gap

from math import *

fC = open('C:\Documents and Settings\Protean\Desktop\C-small-attempt2.in','r')
fOUT = open('C:\Documents and Settings\Protean\Desktop\CC_out.txt','w')

N_cases = int(fC.readline())

Nc = range(N_cases)

# Reading the data

for z in Nc:

    temp = fC.readline()
    t = range(5)
    i = 0
    value = ['','','','','']
    for j in t:
        while (temp[i] != ' ') and (temp[i] != '\n'):
            value[j] = value[j] + temp[i]
            i = i + 1
        value[j] = float(value[j])
        i = i + 1
        
#    print value

# Calculating the probabilities.

    th = value[0] + value[3]            # Modified string thickness
    ra = value[1] - value[2] - value[0] # Modified inner radius

    xy = []
    ti = th
    while (ti <= ra):
        xy.append(ti)
        ti = ti + value[4] + 2*value[3]

    tt = th + value[4] - 2 * value[0]
    while (tt <= ra):
        xy.append(tt)
        tt = tt + value[4] + 2*value[3]

    xy.sort()
    xy.insert(0,0)
 #   print xy
    A1 = 0
    tee = range(len(xy))

    Delta = 0
    Delta1 = 0
    for yem in tee:
        Delta = Delta + pow(-1,yem)*(ra*ra*acos(xy[yem]/ra) - xy[yem]*sqrt(ra*ra-xy[yem]*xy[yem]))/2
        #print xy[yem]
    
#    print Delta

    Grid = [0]
    i = 0
    while(Grid[i] + value[4] < ra + sqrt(2)*th):
        Grid.append(Grid[i] + value[4] + 2*value[3])
        i = i + 1
    Overlap = 0
    sss = range(len(Grid))
    for aa in sss:
        for bb in sss:
            factor = 1.0
            dist = sqrt(Grid[aa]*Grid[aa] + Grid[bb]*Grid[bb])
            if  dist + sqrt(2)*th <= ra:
                factor = factor
            elif dist - sqrt(2)*th < ra:
                factor = factor*((ra-dist)/(sqrt(2)*th)+1)/2
            else:
                factor = 0
            if aa == 0:
                factor = factor/2
            if bb == 0:
                factor = factor/2
#            print dist, sqrt(2)*th, ra, aa, bb, factor
            Overlap = Overlap + factor*th*th*4
    print (2*th*ra-ra*sqrt(ra*ra-th*th)+ra*ra*asin(th/ra))
    # Calculating the probability

    probab = 1 - (ra*ra - 4*(2*Delta - Overlap)/pi)/value[1]/value[1]

    Area1 = pi/4*value[1]*value[1]
    Area2 = pi/4*ra*ra
    if th >= value[4]/2:
        probab = 1
    print 2*Delta/Area1, Overlap/Area1, Area2/Area1, probab

    result = 'Case #' + str(z+1) + ': ' + str(probab) + '\n'
    fOUT.write(result)
#    print th, ra, xy
fC.close()
fOUT.close()
