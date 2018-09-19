#!/usr/bin/env python
# encoding: utf-8

import re

def ginputs(fname):
    fobj = open(fname)
    try:
        L, D, N = tuple([int(x) for x in fobj.readline().split()])

        dct = []

        for i in range(1, D+1): dct.append(fobj.readline().rstrip())
        dct = ','.join(dct)

        for icase in range(1, N+1): 
            ptrn = fobj.readline().rstrip()
            regs = "\(([a-z]+)\)"
            m = re.compile(regs).findall(ptrn)
            for x in m: 
                ptrn = ptrn.replace('(' + x + ')', '(' + '|'.join(list(x)) + ')')
            cnt = len(re.compile(ptrn).findall(dct))
            #yield {'icase': icase, 'cnt': cnt, 'ptrn': ptrn, 'dct': dct}
            yield icase, cnt
    finally:
        fobj.close()


if __name__=='__main__':
    inputfile = r".\inputs\A-large.in"
    for x in ginputs(inputfile):
        print "Case #%d: %d" % x
        #print 
        #print x['icase']
        #print x['ptrn']
        #print x['dct']
        #print x['cnt']
