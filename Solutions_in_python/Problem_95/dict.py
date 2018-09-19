#!/usr/bin/env python

google_dict = {"a": "y",
               "b": "h",
               "c": "e",
               "d": "s",
               "e": "o",
               "f": "c",
               "g": "v",
               "h": "x",
               "i": "d",
               "j": "u",
               "k": "i",
               "l": "g",
               "m": "l",
               "n": "b",
               "o": "k",
               "p": "r",
               "q": "z",
               "r": "t",
               "s": "n",
               "t": "w",
               "u": "j",
               "v": "p",
               "w": "f",
               "x": "m",
               "y": "a",
               "z": "q",
               " ": " ",
               "\n": ""}

def translate(string):
    translated = [ ]
    for s in string:
        translated.append(google_dict[s])

    return "".join(translated)

numtests = None
numcase = 0

f = open('input.txt')
lines = f.readlines()
f.close()

for l in lines:
    if numtests == None:
        numtests = int(l)
    else:
        numcase += 1
        print "Case #%d: %s" % (numcase, translate(l))
        
