#!/usr/bin/env python

from __future__ import division

import collections
import itertools
import sys

class gcj:
    IN = sys.stdin
    number = 0

    @classmethod
    def case(cls):
        cls.number += 1
        return 'Case #%d:' % cls.number

    @classmethod
    def line(cls, type=str):
        line = cls.IN.readline()
        return type(line.strip('\n'))

    @classmethod
    def splitline(cls, type=str):
        line = cls.IN.readline()
        return [type(x) for x in line.split()]



def go(debug = 0):
    pair = []
    x , y = tuple(gcj.splitline(int))
    initform = []
    initform =[ ['@'] * (y+2) ]
    
    #Row Check
    for it in xrange(x):
        t = []
        t = ['@']
        flag = 0
        t.extend(list(str(raw_input())))
        initform.append(t)
        z = initform[-1]
        for i in xrange(1,len(z)-1):
            if z[i] == '#':
                if z[i-1] != '#' and z[i+1] != '#':
                    flag = 1
                else:
                    z[i] = '$'
                    if z[i-1] == '#':
                        z[i-1] = '$'
                    else:
                        z[i+1] ='$'
        z.append('@')
    initform.append(['@'] * (y+2))
    if flag == 1:
        return "Impossible"
    #Column Check

    for i in xrange(1,x+1):
        for j in xrange(1,y+1):
            if initform[i][j] =='#':
                return "Impossible"
            if initform[i][j] == '$':
                if initform[i+1][j] == '$' and initform[i+1][j+1] == '$' and initform[i][j+1] == '$':
                    initform[i][j] = '/'
                    initform[i+1][j] = "\\"
                    initform[i+1][j+1] = '/'
                    initform[i][j+1] = "\\"
                else:
                    return "Impossible"
    for i in xrange(1,x+1):
        for j in xrange(1,y+1):
            if initform[i][j] == '$' or initform[i][j] == '#':
                return "Impossible"
    strr = ""
    for x in initform[1:-1]:
        print "".join(x[1:-1])
    return initform

t = int(raw_input())
debug =0
for x in xrange(t):
    print "Case #%d:" %(x+1)
    if x ==10 or x==11:
        debug = 1 
    else:
        debug = 0
    c = go(debug)
    if c=="Impossible":
        print "Impossible"

