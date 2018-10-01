from __future__ import division

dataset = 'small'
#dataset = 'large'

fin = open('B-%s.in' % dataset, 'r')
fout = open('B-%s.out' % dataset, 'w')

def prime(n):
    """Determine if n is prime."""
    if n in (2, 3, 5, 7, 11, 13, 17, 19):
        return True
    if n%6 not in (1, 5):
        return False
    for i in range(2, n//2):
        if n%i == 0:
            return False
    return True

primeFactorsMem = dict()

def primeFactors(n):
    """Find prime factors of n"""
    try:
        return primeFactorsMem[n]
    except KeyError:
        factors = list()
        for i in range(2,n+1):
            if (n%i==0) and prime(i):
                factors.append(i)
        primeFactorsMem[n] = factors
        return primeFactorsMem[n]

def primeFactorsAtLeast(n, p):
    """Find prime factors of n that are >= p"""
    factors = primeFactors(n)
    return [f for f in factors if f>=p]

ncases = int(fin.readline())
for case in range(1,ncases+1):
    line = fin.readline()
    [a, b, p] = [int(n) for n in line.split(' ')]
    group = dict()
    for i in range(a,b+1):
        group[i] = i
        
    for i in range(a,b+1):
        for j in range(i+1,b+1):
            if group[j] == group[i]:
                # j is already in i's group 
                continue
            facti = set(primeFactorsAtLeast(i,p))
            factj = set(primeFactorsAtLeast(j,p))
            intersect = facti.intersection(factj)
            if intersect:
                g1 = min(group[i], group[j])
                g2 = max(group[i], group[j])
                for k,v in group.items():
                    if v==g2:
                        group[k] = g1
                #print 'grouping %d and %d into group %d (%s)' % (j, i, g1, intersect)
    #print group.values()
    answer = len(set(group.values()))
    #print set(group.values())
    output = 'Case #%d: %d' % (case, answer)
    print output
    fout.write(output+'\n')

fout.close()
