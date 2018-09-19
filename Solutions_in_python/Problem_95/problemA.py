#!/usr/bin/env python2
import sys

letters = {}
lines = open('problemA_dict.txt', 'r').readlines()
for line in range(0, 3):
    i = 0
    for letter in lines[line]:
        letters[letter] = lines[line+3][i]
        i += 1

i = 1
sys.stdin.readline()
lines = sys.stdin.readlines()
for line in lines:
    output = "Case #%d: " % i
    i += 1
    for letter in line.strip():
        output += letters[letter]
    print output
