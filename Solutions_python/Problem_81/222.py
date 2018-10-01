
import sys
import array
from numpy import *


if __name__ == "__main__":
    f = open(sys.argv[1])
    g = open(sys.argv[2],'w')
    t = int(f.readline())
    for _t in range(t):
        n = int(f.readline())
        m = []
        rez=[]
        for i in range(n):
            line = f.readline().strip()
            m.append(list(line))
            s = len([x for x in line if x=='1'])
            total = len([x for x in line if x!='.'])
            rez.append(0.25*float(s)/float(total))
        owp=[]
        indexes=[]
        for i in range(n):
            line = m[i]
            ind = [y for y,x in enumerate(line) if x!='.' ]
            indexes.append(ind)
            o = []
            for j in ind:
                line = m[j]
                s = len([x for y,x in enumerate(line) if x == '1' and i!=y])
                t = len([x for y,x in enumerate(line) if x != '.' and i!=y])
                o.append(float(s)/float(t))
#            print  indexes, o
            owp.append(sum(o)/len(o))
        awg = []
        for i in range(n):
            s=0
            t=0
            for j in indexes[i]:                
                s += owp[j]
                t+=1
            awg = float(s)/(t)
            rez[i]+=0.5*owp[i]+0.25*awg
        print rez
        g.write("Case #%d:\n" % (_t+1))
        for i in range(n):
            g.write("%(n)f\n" % dict(n=rez[i]))
            
#        print awg                   
#        print owp
#        print m
#        print rez
        
