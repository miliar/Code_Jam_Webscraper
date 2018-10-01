import sys
from itertools import combinations

def calc(values, avg):
    m = 0
    n = len(values)
    for x in xrange(n):
        for i in combinations(range(n),x):
#            print i
            if i:
                ss = 0
                l = []
                for y in i:
                    ss = ss ^ values[y]
                    l.append(values[y])
                se = 0
                t = []
                for y in xrange(n):
                    if y in i:
                        continue
                    se = se^values[y]
                    t.append(values[y])
                if se == ss:
                    m = max(m, sum(t), sum(l))
#                    print t, l
#    print m
    return m
if __name__=='__main__':
    fin = sys.stdin
    P = fin.readline()
    for case in xrange(int(P)):
        time = 0
        line = fin.readline()
        N = int(line)
        line = fin.readline()
        values = [int(i) for i in line.split()]
        x = 0
        s = 0
        #calc
        ret = calc(values, s/len(values))
        if ret == 0:
            ret = 'NO'
        print 'Case #%d:' %(case+1), ret


