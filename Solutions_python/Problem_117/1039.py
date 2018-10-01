import itertools
import numpy


with open('/home/vivanov/Downloads/B-large.in') as f:
    lines = f.read().splitlines()[1:]
    l = []
    i = 0
    while i < len(lines) - 1:
        n,m = [int(k) for k in lines[i].split(' ')]
        b = [ [float(k) for k in line.split(' ')] for line in lines[(i+1):(i+1+n)]]
        b = numpy.array(b)
        l.append(b)
        i += n+1
    print l


def not_check(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if not(max(a[:][:,j]) <= a[i][j] or max(a[i]) <= a[i][j]):
                return True


with open('lawnmower_sample.out', 'w') as f :
    to_write = []
    for i in range(len(l)):
        to_write.append(('Case #%s: ' %(i+1)) + ('NO' if not_check(l[i]) else 'YES') + '\n')
    f.writelines(to_write)

    
    
