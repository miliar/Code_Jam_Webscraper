#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Darcy Liu on 2012-04-14.
Copyright (c) 2012 Close To U. All rights reserved.
"""

import sys
import os


def main():
    f = open('A-small-attempt1.in', 'r')
    answer = open('answer.txt', 'r+')
    f.readline()
    n = 1
    source = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv y e q z'
    target = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up a o z q'
    lookup = {}
    for i in range(0,len(source)):
        lookup[source[i]] = target[i] 
        #print i
    #print lookup
    for line in f:
        target = ''
        line = line[:-1]
        for i in range(0,len(line)):
            target += lookup[line[i]]
        s = 'Case #%d: %s\n' % (n,target)
        answer.write(s)
        n += 1


if __name__ == '__main__':
	main()

