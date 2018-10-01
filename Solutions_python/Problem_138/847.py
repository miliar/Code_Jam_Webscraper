#!/usr/bin/env python
# -*- coding:utf-8 -*-
########################
# Google code jam
# Problem A. Magic Trick
# small input
# @Author yangdf
########################
import re


pattern = re.compile(r' +')

def getInput(line):
    '''get float value from input str
    '''
    line = line.strip()
    line = pattern.sub(' ', line)
    line_list = line.split(' ')
    line_list = map(lambda x: float(x), line_list)
    return line_list

def getOrigin(mass_list1, mass_list2):
    count = 0
    mass1 = sorted(mass_list1)
    mass2 = sorted(mass_list2)
    for item1 in mass1:
        item2 = mass2[0]
        if item2 > item1:
            continue
        else:
            count += 1
            mass2 = mass2[1:]
    return count




if __name__ == '__main__':
    t = raw_input()
    for x in xrange(1, int(t)+1):
        line_size = raw_input()
        line = raw_input()
        mass_list1 = getInput(line)
        line = raw_input()
        mass_list2 = getInput(line)
        rst1 = getOrigin(mass_list1, mass_list2)
        rst2 = getOrigin(mass_list2, mass_list1)
        print 'Case #%d: %d %d' % (x, rst1, int(line_size) - rst2)
