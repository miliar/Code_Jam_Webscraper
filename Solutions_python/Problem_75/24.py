#!/usr/bin/env python
import sys

def cal(combine, opposite, seq):
    dCombine = {}
    dOpposite = {}
    for c in combine:
        a=c[0]
        b=c[1]
        dCombine[a+b]=c[2]
        dCombine[b+a]=c[2]
    #print 'dCombine', dCombine
    for c in opposite:
        a=c[0]
        b=c[1]
        la = dOpposite.get(a,[])
        la.append(b)
        dOpposite[a] = la
        lb = dOpposite.get(b,[])
        lb.append(a)
        dOpposite[b] = lb
    #print 'dOpposite', dOpposite
    rs = []
    for s in seq:
        if not len(rs):
            rs.append(s)
        elif dCombine.get(rs[-1]+s,0):
            rs[-1]=dCombine.get(rs[-1]+s)
        else:
            rs.append(s)
            oppo = dOpposite.get(s,[])
            for o in oppo:
                if o in rs[:-1]:
                    rs = []
                    break
    return '['+', '.join(rs)+']'

def wf(fileName,results):
    f = open(fileName,'w')
    for i,r in enumerate(results):
        f.write('Case #%d: %s\n'%(i+1,r))
    f.close()

def rf(fileName):
    f = open(fileName,'r')
    inputs = []
    n = int(f.readline())
    for i in range(n):
        l = f.readline()
        inputs.append(l)
    return inputs
   
if __name__=='__main__':
    inputs = rf(sys.argv[-1])
    #inputs = ['0 0 2 EA']
    #inputs = ['1 QRI 0 4 RRQR']
    #inputs = ['1 QFT 1 QF 7 FAQFDFQ']
    #inputs = ['1 EEZ 1 QE 7 QEEEERA']
    #inputs = ['0 1 QW 2 QW']

    results = []
    for i,ip in enumerate(inputs):
        print i
        #print ip
        ip = ip.split()
        cCombine = int(ip[0])
        combine = ip[1:1+cCombine]
        cOpposite = int(ip[1+cCombine])
        opposite = ip[2+cCombine:2+cCombine+cOpposite]
        seq = ip[-1]
        #print cCombine, combine
        #print cOpposite, opposite
        #print seq
        rt = cal(combine, opposite, seq)
        #print rt 
        if rt:
            results.append(str(rt))
        else:
            results.append('OFF')
    wf(sys.argv[-1][:-2]+'out',results)

