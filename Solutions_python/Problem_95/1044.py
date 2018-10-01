#! /usr/bin/env python
# -*- coding: utf-8 -*-
#gs = (
#'ejp mysljylc kd kxveddknmc re jsicpdrysi',
#'our language is impossible to understand',

#'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
#'there are twenty six factorial possibilities',

#'de kr kd eoya kw aej tysr re ujdr lkgc jv',
#'so it is okay if you want to just give up')

#dic={}

#for i in (0, 2, 4):
    #for j in xrange(len(gs[i])):
        #if gs[i][j] not in dic:
            #dic[gs[i][j]] = gs[i+1][j]

#from pprint import pprint
#pprint(dic)
#from string import lowercase
#for x in lowercase:
    #if x not in dic.keys():
        #print 'key: ', x
    #if x not in dic.values():
        #print 'value: ', x

letters_map = {' ': ' ',
 'a': 'y',
 'b': 'h',
 'c': 'e',
 'd': 's',
 'e': 'o',
 'f': 'c',
 'g': 'v',
 'h': 'x',
 'i': 'd',
 'j': 'u',
 'k': 'i',
 'l': 'g',
 'm': 'l',
 'n': 'b',
 'o': 'k',
 'p': 'r',
 'r': 't',
 's': 'n',
 't': 'w',
 'u': 'j',
 'v': 'p',
 'w': 'f',
 'x': 'm',
 'y': 'a',
 'q': 'z',  # there is no 'q' in keys
 'z': 'q'  # the same with 'q'
 }

if __name__ == '__main__':
    n = int(raw_input())
    for x in xrange(n):
        g = raw_input()
        s = [letters_map[i] for i in g]
        print "Case #%d: %s" % (x + 1, ''.join(s))
