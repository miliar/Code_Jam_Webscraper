#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2014 george 
#
# Distributed under terms of the MIT license.




def process(data):
    c, f, x = data.split()
    c, f, x = float(c), float(f), float(x)
    
    curr = 2
    base = 0

    now = x / curr

    while True:
        base += c/ curr
        last = x / (curr + f) + base
        if now <= last:
            return "%.7f"%now
        else:
            now = last
            curr += f





if __name__ == '__main__':
    data = '''
        4
        30.0 1.0 2.0
        30.0 2.0 100.0
        30.50000 3.14159 1999.19990
        500.0 4.0 2000.0
    '''
    f = open('in', 'r+')
    data = f.read()
    f.close()
    data = data.strip().split('\n')
    total = int(data[0])
    data = data[1:]
    
    for i in xrange(1, total+1):
        print 'Case #{}: {}'.format(i, process(data[i-1]))
