#!/usr/bin/python
import sys

def translate(letter):
    return {
        'a' : 'y',
        'b' : 'h',
        'c' : 'e',
        'd' : 's',
        'e' : 'o',
        'f' : 'c',
        'g' : 'v',
        'h' : 'x',
        'i' : 'd',
        'j' : 'u',
        'k' : 'i',
        'l' : 'g',
        'm' : 'l',
        'n' : 'b',
        'o' : 'k',
        'p' : 'r',
        'q' : 'z',
        'r' : 't',
        's' : 'n',
        't' : 'w',
        'u' : 'j',
        'v' : 'p',
        'w' : 'f',
        'x' : 'm',
        'y' : 'a',
        'z' : 'q'
    }[letter]


input = file('A-small-attempt0.in')
lines = [x.split() for x in input.readlines()]

index = 1
for line in lines[1:]:
    engLine = ''
    for word in line:
        for letter in word:
            engLine += translate(letter)
        engLine += ' '

    print "Case #%d: %s" % (index, engLine)
    index += 1