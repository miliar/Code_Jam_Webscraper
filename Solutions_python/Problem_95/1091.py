#!/usr/bin/env python3
# -*- coding: utf-8 -*-


myDict = {}

sampleInputList = ("ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv")
sampleOutputList = ("our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up")
letters = set("abcdefghijklmnopqrstuvwxyz")

for i in range(len(sampleInputList)):
    string1 = sampleInputList[i]
    string2 = sampleOutputList[i]
    for j in range(len(string1)):
        key = string1[j]
        value = string2[j]
        myDict.setdefault(key, value)
    
myDict.setdefault('y', 'a')
myDict.setdefault('q', 'z')
myDict.setdefault('e', 'o')

missKey = letters - set(myDict.keys())
missValue = letters - set(myDict.values())
myDict.setdefault(missKey.pop(), missValue.pop())

inputFile = open('A-small-attempt0.in.txt', 'r', encoding='utf-8')
outputFile = open('output.txt', 'w', encoding='utf-8')

T = int(inputFile.readline().strip())
for _ in range(T):
    line = inputFile.readline().strip()
    resultLine = "Case #" + str(_ + 1) + ": "
    for char in line:
        resultLine += myDict.get(char, " ")
    resultLine += "\n"
    outputFile.write(resultLine)
    print(resultLine)
    
outputFile.close()