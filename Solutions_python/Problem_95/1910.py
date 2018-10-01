#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Luís Brandão on 2012-04-14.
"""

import sys
import os

def qualificationA():
    input1 = 'ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv'
    translation = 'ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup'
    
    dictionary = dict()
    for i in range(0,len(input1)):
        dictionary[input1[i]] = translation[i]
    dictionary['z'] = 'q'
    dictionary['q'] = 'z'

    inputFile = open("A-small-attempt3.in")
    outputFile = open("qualification-A-luisbrandao.txt","w")
    counter = 0
    cases = 0
    for line in inputFile:
        if counter is 0:
            cases = int(line)
        else:
            line = line.replace('\n','')
            charList = list(line)
            for j in range(0,len(charList)):
                if charList[j] in dictionary.keys():
                    charList[j] = dictionary[charList[j]]
            print 'Case #{0}: {1}'.format(counter,''.join(charList))
            outputFile.write("Case #{0}: {1}".format(counter,''.join(charList)))
            if counter < cases:
                outputFile.write("\n")
        counter = counter + 1

def main():
    qualificationA()


if __name__ == '__main__':
	main()

