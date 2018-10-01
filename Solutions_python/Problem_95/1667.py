#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import sys

input_txt = ['ejp mysljylc kd kxveddknmc re jsicpdrysi',
         'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
         'de kr kd eoya kw aej tysr re ujdr lkgc jv']

output_txt = ['our language is impossible to understand',
          'there are twenty six factorial possibilities',
          'so it is okay if you want to just give up']

map_dict = {'q':'z','z':'q'}
for itxt, otxt in zip(input_txt, output_txt):
    for i, j in zip(itxt, otxt):
        if i==' ': continue
        map_dict[i] = j

cases = sys.stdin.readline()
case = 1
for line in sys.stdin:
    line = line[:-1]
    output = ""
    for i in line:
        if i==' ': output += ' '
        else: output += map_dict[i]
    print "Case #%d: %s" % (case, output)
    case += 1
