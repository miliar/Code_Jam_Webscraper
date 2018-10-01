#!/usr/bin/python

import sys

googlerese_map = {
    "a":"y",
    "b":"h",
    "c":"e",
    "d":"s",
    "e":"o",
    "f":"c",
    "g":"v",
    "h":"x",
    "i":"d",
    "j":"u",
    "k":"i",
    "l":"g",
    "m":"l",
    "n":"b",
    "o":"k",
    "p":"r",
    "q":"z",
    "r":"t",
    "s":"n",
    "t":"w",
    "u":"j",
    "v":"p",
    "w":"f",
    "x":"m",
    "y":"a",
    "z":"q",
    " ":" ",
}


s = u"anil"

mp = {}
for item in googlerese_map.keys():
    mp[ord(unicode(item))] = unicode(googlerese_map[item])

#print mp
#print s.translate(mp)

i=1

lines = open(sys.argv[1]).read().split("\n")

for arg in lines[1:-1]:
    #print arg
    print "Case #%d:" % (i), unicode(arg).translate(mp)
    i = i+1
