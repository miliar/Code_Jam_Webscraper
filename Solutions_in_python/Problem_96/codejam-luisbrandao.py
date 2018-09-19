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

def qualificationB():
    inputFile = open("B-large.in")
    outputFile = open("qualification-Blarge-luisbrandao.txt","w")
    counter = 0
    cases = 0
    res = 0
    for line in inputFile:
        if counter is 0:
            cases = int(line)
        else:
            line = line.replace('\n','')
            line = line.split(' ')
            
            N = line[0]
            S = int(line[1])
            p = int(line[2])
            ts = line[3:len(line)]

            for t in ts:
                if ((p - 1) * 2 + p) == int(t) and p > 0:
                    res = res + 1
                elif ((p + 1) * 2 + p) == int(t) and p < 10:
                    res = res + 1
                elif (p * 3) <= int(t):
                    res = res + 1
                elif (p * 2 + (p-1)) <= int(t) and p > 0:
                    res = res + 1
                elif (p * 2 + (p+1)) <= int(t) and p < 10:
                    res = res + 1
                elif (p + (p - 1) + (p + 1)) == int(t) and S > 0 and p < 10 and p > 0:
                    res = res + 1
                    S = S - 1
                elif (p + (p - 1) + (p - 2)) == int(t) and S > 0 and p > 1:
                    res = res + 1
                    S = S - 1
                elif (p + (p + 1) + (p + 2)) == int(t) and S > 0 and p < 9:
                    res = res + 1
                    S = S - 1
                elif (p + (p - 2) + (p - 2)) == int(t) and S > 0 and p > 1:
                    res = res + 1
                    S = S - 1
                elif (p + (p + 2) + (p + 2)) == int(t) and S > 0 and p < 9:
                    res = res + 1
                    S = S - 1
                        
            print 'Case #{0}: {1}'.format(counter,res)
            outputFile.write("Case #{0}: {1}".format(counter,res))
            if counter < cases:
                outputFile.write("\n")
            
            res = 0
            
        counter = counter + 1


def main():
    # qualificationA()
    qualificationB()

if __name__ == '__main__':
	main()

