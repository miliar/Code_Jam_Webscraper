#!/usr/bin/python
# -*- coding:utf-8 -*-
import os

def count():
    try:
        fin = open("B-large.in", "r")
        fout = open("B-large.out", "w")
        t = int(fin.readline())
        for i in range(t):
            n = 0.0
            f0 = 2
            [c, f, x] = [float(j) for j in fin.readline().strip().split()]
            #print c,f,x
            while x/f0 > (c/f0 + x/(f0+f)):
                n += c/f0
                f0 += f
            n += x/f0
            #print n
            fout.write("Case #%d: %.7f\n"%(i+1, n))
        fin.close()
        fout.close()

    except Exception,e:
        print e
        pass

if __name__ == "__main__":
    count()